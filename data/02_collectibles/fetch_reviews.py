import json, sys, time, urllib.request, re, html
sys.stdout.reconfigure(encoding="utf-8")
H={"User-Agent":"Mozilla/5.0 research"}
APPS={"Collectr":1603892248,"CollX":1581164444,"CoinSnap":1634551626,"Foloy":6770516012,"FoilSnap":6752642525,
"Ludex":1616691213,"PriceCharting":6452190948,"RareCandy":1608616408,"TCGplayer":1247645833,"RockIdentifier":1546796934,
"HoloDex":6747442689,"DragonShield":1199495742}
def get(u):
    for i in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40).read()
        except Exception as e: err=e; time.sleep(4)
    raise err
out={}
for name,aid in APPS.items():
    res=json.loads(get(f"https://itunes.apple.com/lookup?id={aid}&country=us"))["results"]
    lk=res[0] if res else {"trackName":name}
    revs=[]
    for p in range(1,11):
        try:
            d=json.loads(get(f"https://itunes.apple.com/us/rss/customerreviews/page={p}/id={aid}/sortby=mostrecent/json"))
        except Exception as e:
            break
        ents=d.get("feed",{}).get("entry",[])
        if isinstance(ents,dict): ents=[ents]
        ents=[e for e in ents if "im:rating" in e]
        if not ents: break
        for e in ents:
            revs.append({"r":int(e["im:rating"]["label"]),"t":e["title"]["label"],"b":e["content"]["label"],"v":e.get("im:version",{}).get("label"),"d":e.get("updated",{}).get("label","")[:10]})
        time.sleep(1)
    # IAP from app page
    iap=[]
    try:
        h=get(f"https://apps.apple.com/us/app/id{aid}").decode("utf-8","ignore")
        for m in re.finditer(r'"name":"([^"]{2,80})","price":"?([\$0-9.,]+)',h): iap.append((m.group(1),m.group(2)))
        if not iap:
            txt=re.sub(r"<[^>]+>"," ",h); txt=html.unescape(txt)
            i=txt.find("In-App Purchases")
            if i>0: iap=[re.sub(r"\s+"," ",txt[i:i+900])]
    except Exception as e: iap=[f"ERR {e}"]
    out[name]={"id":aid,"title":lk["trackName"],"dev":lk.get("artistName"),"ratings":lk.get("userRatingCount"),"rating":lk.get("averageUserRating"),
               "released":lk.get("releaseDate","")[:10],"updated":lk.get("currentVersionReleaseDate","")[:10],"desc":lk.get("description",""),"iap":iap,"reviews":revs}
    rs=[x["r"] for x in revs]
    print(f"{name}: {len(revs)} reviews, avg {sum(rs)/max(1,len(rs)):.2f}, 1-2★ {sum(r<=2 for r in rs)}, dates {revs[-1]['d'] if revs else ''}..{revs[0]['d'] if revs else ''}, iap {str(iap)[:200]}")
json.dump(out,open("appstore_reviews.json","w",encoding="utf-8"),ensure_ascii=False)
