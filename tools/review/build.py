"""Fill the review page template: python3 -I build.py BATCH nights.json out.html"""
import json, sys
batch, nights, out = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(__file__.replace("build.py", "template.html")).read()
data = json.dumps(json.load(open(nights)), ensure_ascii=False).replace("</", "<\\/")
open(out, "w").write(t.replace("__BATCH__", str(int(batch))).replace("__NIGHTS__", data))
