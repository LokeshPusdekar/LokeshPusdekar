#!/usr/bin/env python3
"""Generate contribution-heatmap.svg from GitHub GraphQL contribution calendar.

Usage:
  python scripts/make_contribution_svg.py --username LokeshPusdekar --token "$PROFILE_TOKEN"

The token is read from the command line only so it never needs to be committed.
"""
import argparse, json, os, urllib.request
from pathlib import Path

Q = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{totalContributions,weeks{contributionDays{contributionCount,date,weekday}}}}}}"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--username", required=True)
    ap.add_argument("--token", default=os.getenv("PROFILE_TOKEN"))
    ap.add_argument("--out", default="contribution-heatmap.svg")
    a = ap.parse_args()
    if not a.token:
        raise SystemExit("Missing --token or PROFILE_TOKEN")

    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": Q, "variables": {"login": a.username}}).encode(),
        headers={"Authorization": f"bearer {a.token}", "Content-Type":"application/json",
                 "User-Agent":"profile-art-generator"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)

    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    total = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]

    # GitHub returns up to 53 weeks, each containing 7 days.
    max_count = max((d["contributionCount"] for w in weeks for d in w["contributionDays"]), default=1)
    palette = ["#161f2b","#0e4429","#006d32","#26a641","#39d353"]

    parts = ["""<svg xmlns="http://www.w3.org/2000/svg" width="860" height="145" viewBox="0 0 860 145">
<rect width="860" height="145" rx="12" fill="#0a1017"/>
<text x="18" y="24" font-family="monospace" font-size="11" fill="#22d3ee">CONTRIBUTION.MAP</text>
<text x="842" y="24" text-anchor="end" font-family="monospace" font-size="10" fill="#718096">LIVE GITHUB DATA</text>
<g transform="translate(18,40)">"""]
    for x, week in enumerate(weeks[-53:]):
        for d in week["contributionDays"]:
            y = int(d["weekday"]) * 15
            c = d["contributionCount"]
            if c == 0: idx = 0
            elif c / max_count <= .25: idx = 1
            elif c / max_count <= .50: idx = 2
            elif c / max_count <= .75: idx = 3
            else: idx = 4
            parts.append(f'<rect x="{x*15}" y="{y}" width="11" height="11" rx="2" fill="{palette[idx]}"><title>{d["date"]}: {c} contributions</title></rect>')
    parts += [f"""</g>
<text x="18" y="138" font-family="monospace" font-size="9" fill="#617488">{total} contributions in the current GitHub contribution window</text>
</svg>"""]
    Path(a.out).write_text("\n".join(parts), encoding="utf-8")

if __name__ == "__main__":
    main()
