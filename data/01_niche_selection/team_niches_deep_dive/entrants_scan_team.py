"""Free overheating metric: for each finalist niche, all US App Store apps returned by iTunes Search (limit 200 per keyword),
grouped by release year; 'traction' = rating count thresholds. Output JSON + printed table."""
import json, sys, time, urllib.parse, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
OUT = sys.argv[1]
H = {"User-Agent": "Mozilla/5.0 (research script; student homework)"}
TERMS = {
    "coparenting": ["co-parenting", "coparenting app", "custody calendar", "co parent messaging"],
    "cleaner": ["photo cleaner", "storage cleaner", "cleanup phone storage", "duplicate photos"],
    "boating": ["boating", "boat maintenance", "marine navigation", "boat log"],
    "rocks": ["rock identifier", "crystal identifier", "rockhounding", "gem identifier"],
}
TERMS_OLD = {
    50: ["card scanner", "coin identifier", "tcg collector", "sports card scanner", "pokemon card scanner", "coin value"],
    55: ["crochet", "knitting", "sewing pattern", "row counter"],
    61: ["family tree", "restore old photos", "photo scanner old photos", "colorize photo"],
    44: ["plant identifier", "plant care"],
    41: ["meal planner", "recipe saver", "pantry"],
    47: ["fishing app", "fish identifier"],
    67: ["rv camping", "road trip planner", "campground"],
    63: ["couples app", "long distance relationship"],
}
GAME_GENRES = {"Games"}
res = {}
for n, terms in TERMS.items():
    seen = {}
    for t in terms:
        url = "https://itunes.apple.com/search?" + urllib.parse.urlencode({"term": t, "country": "us", "entity": "software", "limit": 200})
        for attempt in range(4):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=30)); break
            except Exception:
                time.sleep(10 * (attempt + 1))
        else:
            print(f"  fail {n} {t}"); continue
        for r in d.get("results", []):
            if r.get("primaryGenreName") in GAME_GENRES:
                continue
            seen[r["trackId"]] = {"id": r["trackId"], "price": r.get("formattedPrice"), "name": r["trackName"], "dev": r.get("artistName"), "ratings": r.get("userRatingCount", 0),
                                  "year": int(r.get("releaseDate", "0000")[:4] or 0), "genre": r.get("primaryGenreName")}
        time.sleep(4)
    apps = list(seen.values())
    def stats(sel):
        return {"n": len(sel), "ge1k": sum(a["ratings"] >= 1000 for a in sel), "ge10k": sum(a["ratings"] >= 10000 for a in sel)}
    new = [a for a in apps if a["year"] >= 2024]
    res[n] = {"total": stats(apps), "new_2024_26": stats(new),
              "y2024": stats([a for a in apps if a["year"] == 2024]), "y2025": stats([a for a in apps if a["year"] == 2025]),
              "y2026": stats([a for a in apps if a["year"] == 2026]),
              "top_new": sorted(new, key=lambda a: -a["ratings"])[:8],
              "top_all": sorted(apps, key=lambda a: -a["ratings"])[:12]}
    s = res[n]
    print(f"\n#{n}: всього {s['total']['n']} (≥1K {s['total']['ge1k']}, ≥10K {s['total']['ge10k']}) | нові 2024–26: {s['new_2024_26']['n']} "
          f"(≥1K {s['new_2024_26']['ge1k']}, ≥10K {s['new_2024_26']['ge10k']}) | 2024 {s['y2024']['n']} · 2025 {s['y2025']['n']} · 2026 {s['y2026']['n']}")
    print("   TOP ALL:")
    for a in s["top_all"]:
        print(f"     {a['ratings']:>9,}  {a['year']}  {a['name'][:45]} | {a['dev'][:25]} | id{a['id']}")
    print("   TOP NEW:")
    for a in s["top_new"]:
        print(f"     {a['ratings']:>8,}  {a['year']}  {a['name'][:45]} | {a['dev'][:25]}")
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("DONE")
