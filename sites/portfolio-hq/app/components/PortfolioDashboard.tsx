"use client";

import { useState, type KeyboardEvent } from "react";
import type { PortfolioData } from "../types";
import { Models, Numbers, Overview, Products, Rhythm } from "./PortfolioSections";

const tabs = ["overview", "products", "numbers", "rhythm", "models"] as const;
type Tab = (typeof tabs)[number];

const labels: Record<Tab, string> = {
  overview: "Command",
  products: "Products",
  numbers: "Numbers",
  rhythm: "Rhythm",
  models: "Models",
};

export function PortfolioDashboard({ data }: { data: PortfolioData }) {
  const [active, setActive] = useState<Tab>("overview");

  function handleKeys(event: KeyboardEvent<HTMLDivElement>) {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
    event.preventDefault();
    const current = tabs.indexOf(active);
    const delta = event.key === "ArrowRight" ? 1 : -1;
    setActive(tabs[(current + delta + tabs.length) % tabs.length]);
  }

  return (
    <main role="main" className="site-shell">
      <header className="topbar">
        <div className="brand-block">
          <strong>Portfolio HQ</strong>
          <span>Agentic OS</span>
        </div>
        <div className="snapshot-meta">
          <span className="private-chip">Private founder snapshot</span>
          <time>{data.generatedAt}</time>
        </div>
      </header>

      <div className={`trust-banner ${data.trust.level === "mixed" ? "mixed" : "clear"}`} role="status">
        <span className="trust-dot" aria-hidden="true" />
        <div>
          <strong>{data.trust.label}</strong>
          <p>{data.trust.reasons.join(" ")}</p>
          {data.consistencyIssues.length > 0 && (
            <ul>
              {data.consistencyIssues.map((issue) => (
                <li key={issue.id}><b>{issue.source}:</b> {issue.message}</li>
              ))}
            </ul>
          )}
        </div>
      </div>

      <div className="tabs" role="tablist" aria-label="Portfolio sections" onKeyDown={handleKeys}>
        {tabs.map((tab, index) => (
          <button
            key={tab}
            type="button"
            role="tab"
            id={`tab-${tab}`}
            aria-controls={`panel-${tab}`}
            aria-selected={active === tab}
            tabIndex={active === tab ? 0 : -1}
            onClick={() => setActive(tab)}
          >
            <span>{index + 1}</span>{labels[tab]}
          </button>
        ))}
      </div>

      <div className="content" role="tabpanel" id={`panel-${active}`} aria-labelledby={`tab-${active}`}>
        {active === "overview" && <Overview data={data} />}
        {active === "products" && <Products data={data} />}
        {active === "numbers" && <Numbers data={data} />}
        {active === "rhythm" && <Rhythm data={data} />}
        {active === "models" && <Models data={data} />}
      </div>
    </main>
  );
}
