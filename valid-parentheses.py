str="([{}])"
hashset=[]
hashmap={")" : "(",
         "]" : "[",
         "}" : "{"}
for c in str:
    if c in hashmap:
        if hashset and hashset[-1]==hashmap[c]:
            hashset.pop()
        else:
            print(False)
            break
    else:
        hashset.append(c)
else:
    if len(hashset)==0:
        print(True)
    else:
        print(False)
