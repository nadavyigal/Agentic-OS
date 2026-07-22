#!/usr/bin/env python3
"""Generate the Builder OS Brain Map — a clickable Excalidraw drawing of the
real vault link graph.

Founder-approved vault automation (2026-07-12). Reads every note in the vault,
resolves wikilinks (alias-aware), lays the notes out as constellations grouped
by domain, and writes an Excalidraw-plugin markdown file where:

  - every node is a real note, sized by how many other notes link to it
  - every edge is a real [[wikilink]] that exists in the vault today
  - every node carries `link: [[Title]]` — clicking it in Obsidian jumps to
    the actual note
  - colors match the semantic color groups configured in .obsidian/graph.json,
    so graph view and the Brain Map speak the same color language

Fully deterministic (positions/ids/seeds are hashes of note names, no
timestamps, no randomness): re-running with an unchanged vault produces an
identical file, so a refresh-triggered regeneration only creates a git diff
when the knowledge graph itself changed.

Output: <vault>/01-Agentic-OS/Maps/Builder OS Brain Map.md
Usage:  python3 scripts/brain_map/generate_brain_map.py
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "agentic_os"))
import vault_git  # noqa: E402  (sibling helper package; added to path above)

VAULT = Path("/Users/nadavyigal/Documents/Projects /Nadav Builder OS")
OUT = VAULT / "01-Agentic-OS" / "Maps" / "Builder OS Brain Map.md"
SKIP_DIRS = {".claude", ".obsidian", ".git", ".trash", "docs"}
SKIP_FOLDERS = ("09-Templates", "10-Archive")

# category -> (label, angle degrees, radius, stroke, background)
CATEGORIES = {
    "core":     ("Home & Index",      0,    0, "#1e1e1e", "#f1f0eb"),
    "research": ("Research",         25, 1500, "#185FA5", "#E6F1FB"),
    "os":       ("Agentic OS",       80, 1450, "#534AB7", "#EEEDFE"),
    "decisions":("Decisions & Lessons",125,1500, "#854F0B", "#FAEEDA"),
    "prompts":  ("Prompts",         165, 1500, "#5F5E5A", "#F1EFE8"),
    "runsmart": ("RunSmart",        205, 1550, "#0F6E56", "#E1F5EE"),
    "products": ("Other Products",  250, 1500, "#3B6D11", "#EAF3DE"),
    "rhythm":   ("Weekly & Journal",290, 1500, "#993556", "#FBEAF0"),
    "resumely": ("Resumely",        335, 1550, "#993C1D", "#FAECE7"),
}
LIVING_PAGES = {"RunSmart", "ResumeBuilder"}


def category_for(rel: str) -> str:
    if rel.startswith("02-Products/RunSmart"):
        return "runsmart"
    if rel.startswith("02-Products/ResumeBuilder"):
        return "resumely"
    if rel.startswith("02-Products"):
        return "products"
    if rel.startswith("01-Agentic-OS"):
        return "os"
    if rel.startswith("03-Research"):
        return "research"
    if rel.startswith("04-Prompts"):
        return "prompts"
    if rel.startswith(("05-Decisions", "08-Lessons-Learned")):
        return "decisions"
    if rel.startswith(("07-Weekly-Reviews", "11-Journal", "00-Inbox")):
        return "rhythm"
    return "core"  # root-level Home/Dashboard/wiki files


def h32(s: str) -> int:
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) % (2**31 - 1) + 1


def hid(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()[:16]


def base_el(eid: str, etype: str, x: float, y: float, w: float, h: float, **kw) -> dict:
    el = {
        "id": eid, "type": etype,
        "x": round(x, 1), "y": round(y, 1),
        "width": round(w, 1), "height": round(h, 1),
        "angle": 0,
        "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid",
        "roughness": 1, "opacity": 100,
        "groupIds": [], "frameId": None, "roundness": None,
        "seed": h32(eid + "seed"), "version": 1, "versionNonce": h32(eid + "nonce"),
        "isDeleted": False, "boundElements": None, "updated": 1,
        "link": None, "locked": False,
    }
    el.update(kw)
    return el


def text_el(eid: str, x: float, y: float, text: str, size: int, color: str,
            align: str = "center", link: str | None = None) -> dict:
    w = max(10.0, 0.62 * size * max(len(line) for line in text.split("\n")))
    h = 1.25 * size * (text.count("\n") + 1)
    el = base_el(eid, "text", x - (w / 2 if align == "center" else 0), y, w, h,
                 strokeColor=color, link=link)
    el.update({
        "text": text, "rawText": text, "originalText": text,
        "fontSize": size, "fontFamily": 1,
        "textAlign": align, "verticalAlign": "top",
        "containerId": None, "lineHeight": 1.25, "baseline": size,
    })
    return el


def scan_vault():
    notes: dict[str, str] = {}      # title -> rel path
    aliases: dict[str, str] = {}    # alias -> title
    bodies: dict[str, str] = {}     # title -> raw text
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, f), VAULT)
            if rel.startswith(SKIP_FOLDERS):
                continue
            # The map must not scan itself: its scene JSON embeds [[links]] to
            # every note, which would make it a fake mega-hub and break the
            # unchanged-vault -> identical-output determinism guarantee.
            if (VAULT / rel) == OUT:
                continue
            title = f[:-3]
            # File-sync conflict copies ("CLAUDE 2.md" beside "CLAUDE.md") are
            # shadows of a real note, not notes: mapping them produces phantom
            # "[[Title 2]]" nodes, and a synced copy of this map itself embeds
            # [[links]] to every note, turning it into a fake mega-hub.
            m = re.fullmatch(r"(.+) \d+", title)
            if m and os.path.exists(os.path.join(root, m.group(1) + ".md")):
                continue
            notes[title] = rel
            txt = Path(root, f).read_text(errors="ignore")
            bodies[title] = txt
            fm = re.match(r"^---\n(.*?)\n---", txt, re.S)
            if fm and "aliases:" in fm.group(1):
                block = fm.group(1).split("aliases:", 1)[1]
                block = re.split(r"\n[a-zA-Z_-]+:", block, maxsplit=1)[0]
                for a in re.findall(r"^\s*-\s*(.+?)\s*$", block, re.M):
                    aliases[a.strip("\"'")] = title
    return notes, aliases, bodies


# Catalog notes list everything by design; drawing their outlinks would bury
# the genuine idea-to-idea connections under a table of contents. Their nodes
# stay on the map; their outgoing edges don't count.
CATALOG_SOURCES = {"wiki-index", "wiki-log"}


def build_graph(notes, aliases, bodies):
    link_re = re.compile(r"\[\[([^\]\|#]+)")
    edges: set[tuple[str, str]] = set()
    inlinks: dict[str, int] = {t: 0 for t in notes}
    for src, txt in bodies.items():
        if src in CATALOG_SOURCES:
            continue
        for m in link_re.finditer(txt):
            raw = m.group(1).strip()
            tgt = raw if raw in notes else aliases.get(raw)
            if tgt and tgt != src:
                if (src, tgt) not in edges:
                    edges.add((src, tgt))
                    inlinks[tgt] += 1
    return edges, inlinks


def layout(notes, inlinks):
    pos: dict[str, tuple[float, float, float]] = {}  # title -> (x, y, radius)
    by_cat: dict[str, list[str]] = {c: [] for c in CATEGORIES}
    for t, rel in notes.items():
        by_cat[category_for(rel)].append(t)
    golden = math.pi * (3 - math.sqrt(5))
    for cat, (label, angle_deg, dist, *_rest) in CATEGORIES.items():
        members = sorted(by_cat[cat], key=lambda t: (-inlinks[t], t))
        a = math.radians(angle_deg)
        cx, cy = dist * math.cos(a), -dist * math.sin(a)
        for i, t in enumerate(members):
            r_node = 22 + 9 * math.log2(1 + inlinks[t])
            if t in LIVING_PAGES:
                r_node = max(r_node, 62)
            spiral_r = 90 * math.sqrt(i)
            sa = i * golden + h32(t) % 7 * 0.05
            pos[t] = (cx + spiral_r * math.cos(sa), cy + spiral_r * math.sin(sa), r_node)
    return pos, by_cat


def generate() -> str:
    notes, aliases, bodies = scan_vault()
    edges, inlinks = build_graph(notes, aliases, bodies)
    pos, by_cat = layout(notes, inlinks)
    elements: list[dict] = []
    text_index: list[tuple[str, str]] = []  # (text, id) for the Text Elements section

    def add_text(eid, x, y, text, size, color, align="center", link=None):
        elements.append(text_el(eid, x, y, text, size, color, align, link))
        text_index.append((text.replace("\n", " "), eid[:8]))

    # 1. cluster halos + labels (bottom layer)
    for cat, (label, _a, _d, stroke, bg) in CATEGORIES.items():
        members = by_cat[cat]
        if not members:
            continue
        xs = [pos[t][0] for t in members]
        ys = [pos[t][1] for t in members]
        cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
        spread = max(
            max((math.dist((cx, cy), (pos[t][0], pos[t][1])) + pos[t][2]) for t in members),
            160,
        ) + 110
        elements.append(base_el(
            hid("halo:" + cat), "ellipse",
            cx - spread, cy - spread, spread * 2, spread * 2,
            strokeColor=stroke, backgroundColor=bg,
            strokeStyle="dashed", strokeWidth=1, opacity=30, fillStyle="solid",
        ))
        n_notes = len(members)
        add_text(hid("halolabel:" + cat), cx, cy - spread - 56,
                 f"{label} ({n_notes})", 34, stroke)

    # 2. edges (real wikilinks)
    for src, tgt in sorted(edges):
        x1, y1, _ = pos[src]
        x2, y2, _ = pos[tgt]
        el = base_el(hid(f"edge:{src}->{tgt}"), "line",
                     x1, y1, x2 - x1, y2 - y1,
                     strokeColor="#868e96", strokeWidth=1, opacity=25)
        el.update({
            "points": [[0, 0], [round(x2 - x1, 1), round(y2 - y1, 1)]],
            "lastCommittedPoint": None,
            "startBinding": None, "endBinding": None,
            "startArrowhead": None, "endArrowhead": None,
        })
        elements.append(el)

    # 3. nodes — every one clickable
    for t, rel in sorted(notes.items()):
        x, y, r = pos[t]
        cat = category_for(rel)
        stroke, bg = CATEGORIES[cat][3], CATEGORIES[cat][4]
        link = f"[[{t}]]"
        if t in LIVING_PAGES:
            elements.append(base_el(hid("ring:" + t), "ellipse",
                                    x - r - 8, y - r - 8, (r + 8) * 2, (r + 8) * 2,
                                    strokeColor=stroke, strokeWidth=1,
                                    strokeStyle="dashed", opacity=80))
        elements.append(base_el(hid("node:" + t), "ellipse",
                                x - r, y - r, r * 2, r * 2,
                                strokeColor=stroke, backgroundColor=bg,
                                strokeWidth=2 if inlinks[t] >= 3 else 1,
                                fillStyle="solid", link=link))
        label = t if len(t) <= 30 else t[:29] + "…"
        if t in LIVING_PAGES:
            label = "⭐ " + label
        size = 20 if t in LIVING_PAGES else (16 if inlinks[t] >= 3 else 11)
        add_text(hid("label:" + t), x, y + r + 6, label, size, stroke, link=link)

    # 4. title block
    add_text(hid("title"), 0, -2750, "Builder OS — Brain Map", 58, "#1e1e1e")
    add_text(hid("subtitle"), 0, -2660,
             f"{len(notes)} notes · {len(edges)} real links · every node is clickable",
             22, "#5F5E5A")
    add_text(hid("footer"), 0, -2610,
             "drawn from the vault's actual wikilinks · regenerate: ./agentic-os brainmap",
             15, "#868e96")

    scene = {
        "type": "excalidraw",
        "version": 2,
        "source": "agentic-os-brain-map",
        "elements": elements,
        "appState": {"gridSize": None, "viewBackgroundColor": "#ffffff"},
        "files": {},
    }
    text_section = "\n".join(f"{txt} ^{ref}" for txt, ref in text_index)
    return f"""---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Excalidraw Data

## Text Elements
{text_section}

%%
## Drawing
```json
{json.dumps(scene, ensure_ascii=False)}
```
%%
"""


def main() -> int:
    if not VAULT.is_dir():
        print("⚠️ brain map: vault not found, skipped")
        return 0
    # A map generated from a stale checkout depicts a vault state that never
    # existed — exactly what happened on 2026-07-22 (129 nodes drawn from a
    # checkout missing the July 13-19 notes). Refuse rather than mislead.
    if not vault_git.require_fresh_vault(VAULT, "brain map"):
        return 1
    content = generate()
    if OUT.exists() and OUT.read_text() == content:
        print("brain map: unchanged (graph identical), left as-is")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content)
    print(f"brain map: regenerated {OUT.relative_to(VAULT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
