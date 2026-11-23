"""Stage 1: free iTunes Search API scan of niches 34–67 (US App Store). Saves JSON + prints top apps per niche."""
import json, sys, time, urllib.parse, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
OUT = sys.argv[1]
TERMS = {
    34: ["summer camp finder", "kids activities near me", "kids activity scheduler"],
    35: ["IEP special needs", "special needs parenting"],
    36: ["home maintenance", "home maintenance tracker"],
    37: ["car maintenance tracker", "car expenses"],
    38: ["renter tenant", "rental move in checklist"],
    39: ["first time home buyer", "home buying"],
    40: ["home inventory"],
    41: ["pantry food waste", "grocery list", "meal planner"],
    42: ["moving planner", "moving checklist"],
    43: ["smart home setup", "smart home"],
    44: ["plant identification", "plant care", "aquarium aquascape"],
    45: ["bird identification", "birding"],
    46: ["sourdough", "homebrew beer", "fermentation"],
    47: ["fishing", "fish identifier"],
    48: ["hiking", "hiking trails"],
    49: ["garden planner", "gardening"],
    50: ["card scanner", "coin identifier", "collectibles", "sneaker", "vinyl collection", "watch collection"],
    51: ["wine", "whiskey", "coffee journal"],
    52: ["photography lessons", "photo critique"],
    53: ["reseller", "crosslisting", "thrift resale"],
    54: ["board game"],
    55: ["knitting", "crochet", "sewing pattern"],
    56: ["group trip planner", "split expenses"],
    57: ["meetup", "run club", "book club"],
    58: ["pickleball", "padel"],
    59: ["HOA", "neighbors"],
    60: ["family stories", "memoir", "legacy"],
    61: ["family tree", "photo restore", "old photo"],
    62: ["wedding planner"],
    63: ["long distance relationship", "couples app"],
    64: ["alumni"],
    65: ["digital nomad"],
    66: ["accessible travel", "wheelchair"],
    67: ["road trip planner", "EV charging", "RV camping"],
}
res = {}
for n, terms in TERMS.items():
    seen = {}
    for t in terms:
        url = "https://itunes.apple.com/search?" + urllib.parse.urlencode({"term": t, "country": "us", "entity": "software", "limit": 15})
        for attempt in range(3):
            try:
                d = json.load(urllib.request.urlopen(url, timeout=25)); break
            except Exception as e:
                time.sleep(8)
        else:
            continue
        for r in d.get("results", []):
            seen[r["trackId"]] = {"name": r["trackName"], "dev": r.get("artistName"), "ratings": r.get("userRatingCount", 0),
                                  "rating": r.get("averageUserRating"), "price": r.get("formattedPrice"),
                                  "released": r.get("releaseDate", "")[:10], "genre": r.get("primaryGenreName"), "term": t}
        time.sleep(3)
    top = sorted(seen.items(), key=lambda kv: -kv[1]["ratings"])[:8]
    res[n] = [dict(id=k, **v) for k, v in top]
    print(f"\n#{n}")
    for a in res[n][:6]:
        print(f"  {a['ratings']:>9,}  {a['name'][:42]:42s} | {a['dev'][:24]:24s} | {a['released'][:4]} | {a['genre']}")
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
