strs=["ate","eat","tea","cat","tac","act","bat"]
res = {}                                #store group anagrams
for s in strs:
    count={}                            #count each character in string
    for c in s:
        count[c] = count.get(c,0) + 1   #updates character frequency
    key = tuple(sorted(count.items()))  #creates a unique key for each group
    if key in res:
        res[key].append(s)              #add string to existing group
    else:
        res[key] = [s]                  #creates a new group

print(list(res.values()))               #print all anagram groups