str="([{}])"
hashset=[]
hashmap={")" : "(",
         "]" : "[",
         "}" : "{"}
for c in str:
    if c in hashmap:                            #check if current character is closing bracket
        if hashset and hashset[-1]==hashmap[c]: #check if stack is not empty and top matches opening bracket
            hashset.pop()                       #remove matching opening bracket
        else:
            print(False)
            break
    else:
        hashset.append(c)                       #push opening bracket into stack
else:
    if len(hashset)==0:
        print(True)                             #all bracket are properly matched
    else:
        print(False)                            #some opening brackets are still unmatched
