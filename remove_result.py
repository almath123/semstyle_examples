import json

data = json.load(open("semstyle_results_and_baselines.json", "r"))

remove = ["0%d_" % i for i in xrange(1,6)]

ndata = []
for row in data:
    keys = row.keys()
    new_keys = []
    for k in keys:
        fail = False
        for r in remove:
            if k.startswith(r):
                fail = True
        if not fail:
            new_keys.append(k)

    nrow = {}
    for k in new_keys:
        nrow[k] = row[k]
    ndata.append(nrow)

json.dump(ndata, open("semstyle_results.json", "w"))

