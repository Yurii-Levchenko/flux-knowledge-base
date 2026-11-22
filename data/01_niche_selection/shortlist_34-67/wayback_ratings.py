"""Free multi-year momentum: US App Store rating counts from Wayback Machine snapshots (≈ every Jan/Jul 2022–2026)
+ current value from iTunes Lookup API. Output JSON: {app: [{date, ratings, url}]}"""
import json, re, sys, time, urllib.parse, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
OUT = sys.argv[1]
H = {"User-Agent": "Mozilla/5.0 (research script; student homework)"}
APPS = [  # niche, name, id, slug prefixes to search in timemap
    (50, "Collectr", 1603892248, ["collectr"]),
    (50, "CoinSnap", 1634551626, ["coinsnap", "coin-snap"]),
    (50, "CollX", 1581164444, ["collx"]),
    (50, "Coin ID", 1665672552, ["coin-id", "coinid"]),
    (55, "YarnPal", 6738537088, ["yarnpal"]),
    (55, "Loopsy", 6745416564, ["loopsy"]),
    (55, "Sewpal", 6754315885, ["sewpal"]),
    (61, "Photomyne", 1037784828, ["photo-scan", "photomyne", "photoscan"]),
    (61, "Ancestry", 349554263, ["ancestry"]),
    (61, "MyHeritage", 477971748, ["myheritage"]),
    (44, "PictureThis", 1252497129, ["picturethis"]),
    (41, "ReciMe", 1593779280, ["recime"]),
    (47, "Fishbrain", 477967747, ["fishbrain"]),
    (47, "Fish AI", 6740141927, ["fish-ai"]),
    (67, "The Dyrt", 1187626329, ["the-dyrt"]),
    (63, "Paired", 1469609343, ["paired"]),
]
TARGETS = ["20220115", "20220715", "20230115", "20230715", "20240115", "20240715", "20250115", "20250715", "20260115", "20260715"]


def get(url, timeout=60, tries=3):
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=timeout).read()
        except Exception as e:
            err = e
            time.sleep(5 * (i + 1))
    raise err


def decode(b):
    import gzip, zlib
    if b[:2] == b"\x1f\x8b":
        b = gzip.decompress(b)
    else:
        try:
            b = zlib.decompress(b)
        except Exception:
            pass
    return b.decode("utf-8", "ignore")


def parse_count(html):
    for pat in [r'"reviewCount"\s*:\s*(\d+)', r'"ratingCount"\s*:\s*(\d{3,})', r'"userRatingCount"\s*:\s*(\d+)']:
        m = re.search(pat, html)
        if m:
            return int(m.group(1)), "exact"
    m = re.search(r'([\d.,]+)\s*([KkMm]?)\s*Ratings', html)
    if m:
        v = float(m.group(1).replace(",", ""))
        mult = {"k": 1e3, "m": 1e6}.get(m.group(2).lower(), 1)
        return int(v * mult), "rounded"
    return None, None


ONLY = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
res = {}
for niche, name, aid, prefixes in APPS:
    if ONLY and name not in ONLY:
        continue
    rows = []
    for p in prefixes:
        u = ("https://web.archive.org/web/timemap/json?" + urllib.parse.urlencode(
            {"url": f"apps.apple.com/us/app/{p}", "matchType": "prefix", "fl": "timestamp,original,statuscode", "limit": "2000"}))
        try:
            data = json.loads(get(u, 90) or b"[]")
        except Exception as e:
            print(f"  timemap fail {name} {p}: {e}")
            continue
        rows += [r for r in data[1:] if f"id{aid}" in r[1] and r[2] == "200" and "%5C" not in r[1]]
        time.sleep(2)
    rows = sorted({r[0]: r for r in rows}.values())
    picks = []
    for t in TARGETS:
        cand = [r for r in rows if abs(int(r[0][:8]) - int(t)) < 400 and r[0][:6] >= t[:4] + ("01" if t[4:6] == "01" else "06")]
        # nearest capture within ±~3 months of target
        def dist(r):
            from datetime import date
            a = date(int(r[0][:4]), int(r[0][4:6]), int(r[0][6:8])); b = date(int(t[:4]), int(t[4:6]), int(t[6:8]))
            return abs((a - b).days)
        near = sorted(rows, key=dist)
        if near and dist(near[0]) <= 95 and near[0] not in picks:
            picks.append(near[0])
    out = []
    for ts, orig, _ in picks:
        snap = f"https://web.archive.org/web/{ts}id_/{orig}"
        try:
            html = decode(get(snap, 60))
            c, kind = parse_count(html)
        except Exception as e:
            c, kind = None, f"ERR {e}"
        out.append({"date": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", "ratings": c, "kind": kind,
                    "url": f"https://web.archive.org/web/{ts}/{orig}"})
        time.sleep(1.5)
    # current value (iTunes Lookup, free)
    try:
        lk = json.loads(get(f"https://itunes.apple.com/lookup?id={aid}&country=us", 30))["results"][0]
        out.append({"date": "2026-11-08", "ratings": lk.get("userRatingCount"), "kind": "itunes_api",
                    "url": lk.get("trackViewUrl", "").split("?")[0], "released": lk.get("releaseDate", "")[:10]})
    except Exception as e:
        out.append({"date": "2026-11-08", "ratings": None, "kind": f"ERR {e}"})
    res[name] = {"niche": niche, "id": aid, "series": out}
    print(f"\n{niche} {name} ({len(rows)} captures)")
    for o in out:
        print(f"   {o['date']}  {o['ratings'] if o['ratings'] is not None else '—':>10}  {o['kind']}")
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("DONE")
