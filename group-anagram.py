strs=["Ate","eAt","tea","cat","tac","act","bat"]
res = {}
for s in strs:
    count={}
    for c in s:
        count[c] = count.get(c,0) + 1
    key = tuple(sorted(count.items()))
    if key in res:
        res[key].append(s)
    else:
        res[key] = [s]

print(list(res.values()))