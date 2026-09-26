strs=("Manish#", "#manish")
#convet list of strings into a single ASCII encoded string
def encode(strs):
    res=""
    for s in strs:
        for c in s:
            #covert every character to its ASCII value
            res+= str(ord(c))+ ","
        res+="#"        # '#' is used as delimiter
    return res
print(encode(strs))
encoded=encode(strs)
#Decode ASCII sring back into original words
def decode(strs):
    res,i=[],0
    word=""
    num=""
    while i < len(strs):
        if strs[i].isdigit():
            num+= strs[i]
        elif strs[i]==",":
            #convert collected ASCII numbers to character
            word+= chr(int(num))
            num=""
        elif strs[i]=="#":
            #stop completed word
            res.append(word)
            word=""
        i+=1
    return res
print(decode(encoded))
