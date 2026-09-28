#!/usr/bin/env python3
"""Starting capture for visual review: desktop, phone and reduced-motion screenshots plus quick checks.

Usage:
  python scripts/screenshot.py <url-or-html-path> [--out DIR] [--full] [--wait MS] [--scroll N]

Examples:
  python scripts/screenshot.py index.html --out shots
  python scripts/screenshot.py http://localhost:4321 --out shots --scroll 4

What it does: captures the initial desktop (1440px), phone (390px) and reduced-motion (desktop + phone)
states; with --scroll N it also captures N evenly spaced scroll positions at desktop width. It reports
horizontal overflow, JS errors and, for local files, markup after </html>.

What it does NOT do: click, drag, type or test exports. Check key interactions yourself (with reduced
motion emulated too). Serve built sites over HTTP rather than file:// when assets expect a base path.

Requires Python Playwright with a Chromium build. If the browser isn't available, say "not visually
checked". A screenshot only counts once you've looked at it.
"""
import argparse
import pathlib
import re
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="URL or path to an .html file")
    ap.add_argument("--out", default="shots", help="output folder (default: shots)")
    ap.add_argument("--full", action="store_true", help="capture the full page height")
    ap.add_argument("--wait", type=int, default=1200, help="ms to wait after load for animations to settle")
    ap.add_argument("--scroll", type=int, default=0, help="also capture N scroll positions at desktop width")
    args = ap.parse_args()

    target = args.target
    p = pathlib.Path(target)
    if p.exists():
        html = p.read_text(encoding="utf-8", errors="ignore")
        tail = re.split(r"</html\s*>", html, flags=re.I)
        if len(tail) > 1 and tail[-1].strip():
            print("WARNING: content after </html> (move it inside <body>)")
        target = p.resolve().as_uri()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright isn't installed, so the page wasn't visually checked.", file=sys.stderr)
        return 2

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    runs = [
        ("desktop", {"width": 1440, "height": 900}, "no-preference"),
        ("phone", {"width": 390, "height": 844}, "no-preference"),
        ("desktop-reduced-motion", {"width": 1440, "height": 900}, "reduce"),
        ("phone-reduced-motion", {"width": 390, "height": 844}, "reduce"),
    ]
    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception as e:  # browser binary missing, sandbox refused, etc.
            print(f"Couldn't launch a browser ({e}), so the page wasn't visually checked.", file=sys.stderr)
            return 2
        for name, viewport, motion in runs:
            page = browser.new_page(viewport=viewport, reduced_motion=motion)
            errors = []
            page.on("pageerror", lambda exc, errors=errors: errors.append(str(exc)))
            page.goto(target, wait_until="networkidle")
            page.wait_for_timeout(args.wait)
            overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
            path = out / f"{name}.png"
            page.screenshot(path=str(path), full_page=args.full)
            note = f" | horizontal overflow {overflow}px" if overflow > 0 else ""
            errs = f" | JS errors: {errors}" if errors else ""
            print(f"{path}{note}{errs}")
            if name == "desktop" and args.scroll > 0:
                height = page.evaluate("document.documentElement.scrollHeight - window.innerHeight")
                for i in range(1, args.scroll + 1):
                    y = int(height * i / args.scroll)
                    page.evaluate(f"window.scrollTo(0, {y})")
                    page.wait_for_timeout(700)
                    sp = out / f"desktop-scroll-{i}.png"
                    page.screenshot(path=str(sp))
                    print(sp)
            page.close()
        browser.close()
    print("Now open and inspect each screenshot, then click through the main actions yourself.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
