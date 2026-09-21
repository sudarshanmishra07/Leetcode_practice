strs=("sudarshan", "mishra")
def encode(strs):
    res=""
    for s in strs:
        for c in s:
            res+= str(ord(c))+ ","
        res+="#"
    return res
print(encode(strs))
encoded=encode(strs)
def decode(strs):
    res,i=[],0
    word=""
    num=""
    while i < len(strs):
        if strs[i].isdigit():
            num+= strs[i]
        elif strs[i]==",":
            word+= chr(int(num))
            num=""
        elif strs[i]=="#":
            res.append(word)
            word=""
        i+=1
    return res
print(decode(encoded))
