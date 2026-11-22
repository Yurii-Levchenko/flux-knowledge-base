import json,re,sys,collections
sys.stdout.reconfigure(encoding="utf-8")
d=json.load(open("appstore_reviews.json",encoding="utf-8"))
TH={
 "paywall/charges/refund":r"subscri|paywall|charg|refund|cancel|trial|scam|rip ?off|money|pay |paid|price increase|\$\d",
 "scan accuracy":r"wrong card|misidentif|identif\w* wrong|can'?t (scan|recogn)|won'?t scan|doesn'?t (scan|recogn)|scan(ner|s|ning)? (is|are|doesn|don|never|keeps|won|not)|inaccurate scan|wrong (set|version|year|coin|rock|player)|recogni",
 "price accuracy":r"(price|value|pricing)s? (is|are|were|was)? ?(wrong|off|inaccurate|outdated|not accurate|way)|inaccurate (price|value)|overvalu|undervalu|not accurate|wrong price|market price",
 "bugs/crash/data loss":r"crash|bug|glitch|freez|slow|lag|lost (my|all)|disappear|gone|deleted|sync|log ?in|sign ?in|won'?t load|not loading|update (broke|ruin)",
 "grading":r"grad(e|ing)|psa|bgs|cgc|condition|centering",
 "missing cards/sets/langs":r"missing|not (in|listed)|japanese|can'?t find|doesn'?t have|no (option|way)|database",
 "marketplace/selling":r"sell|seller|buyer|ship|marketplace|fee|listing|order",
 "support":r"support|customer service|no response|email",
 "ads":r"\bads?\b|advert",
 "bulk/speed of scanning":r"bulk|batch|multiple cards|one at a time|faster|speed",
 "portfolio/export/tracking":r"portfolio|export|csv|spreadsheet|track(ing)? (my|collection|value)|collection value",
}
rows=[]
for app,v in d.items():
  revs=v["reviews"]
  if not revs: continue
  low=[r for r in revs if r["r"]<=2]; high=[r for r in revs if r["r"]>=4]
  c=collections.Counter(); ch=collections.Counter()
  for r in low:
    t=(r["t"]+" "+r["b"]).lower()
    for k,p in TH.items():
      if re.search(p,t): c[k]+=1
  for r in high:
    t=(r["t"]+" "+r["b"]).lower()
    for k,p in TH.items():
      if re.search(p,t): ch[k]+=1
  print(f"\n## {app}: n={len(revs)} low={len(low)} high={len(high)} period {revs[-1]['d']}..{revs[0]['d']}")
  print("  LOW :", ", ".join(f"{k} {c[k]} ({c[k]*100//max(1,len(low))}%)" for k,_ in c.most_common(7)))
  print("  HIGH:", ", ".join(f"{k} {ch[k]}" for k,_ in ch.most_common(5)))
json.dump(TH,open("themes.json","w"),indent=1)
