#!/usr/bin/env python3
"""Serve the Portfolio HQ dashboard for the Claude preview pane.

Why this exists instead of `python3 -m http.server --directory dashboard`:

`http.server`'s CLI builds its argument parser with
`parser.add_argument('--directory', default=os.getcwd(), ...)`. argparse
evaluates that default at parse time even when --directory IS supplied, so the
module unconditionally calls os.getcwd(). When the preview server is spawned
with a cwd it cannot resolve (macOS returns EPERM traversing the parent dirs
under Documents/), that call raises PermissionError and the server dies before
binding. `cd` in a shell wrapper does not help, because the shell itself needs
getcwd() to start.

This script chdir()s to a known-good absolute directory FIRST. chdir does not
need to read the current cwd, so it works from an unresolvable one.

Port comes from $PORT (the preview harness assigns it via autoPort). 0 lets the
OS pick a free port, which is then printed so the harness can pick it up.
"""
from __future__ import annotations

import functools
import http.server
import os
import socketserver
import sys

DASHBOARD = "/Users/nadavyigal/Documents/Projects /Agentic OS/dashboard"


def main() -> int:
    # Must happen before anything else touches the cwd.
    os.chdir(DASHBOARD)

    try:
        port = int(os.environ.get("PORT") or 0)
    except ValueError:
        port = 0

    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler, directory=DASHBOARD
    )
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        bound = httpd.server_address[1]
        print(f"Serving Portfolio HQ from {DASHBOARD}", flush=True)
        print(f"Listening on http://127.0.0.1:{bound}/portfolio-hq.html", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
