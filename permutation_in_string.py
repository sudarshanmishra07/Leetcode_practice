class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        stck = []
        k = len(s1)
        if k > len(s2):                     #check for edge case
            return False
        for i in range(k):
            stck.append(s2[i])              #store first window
        if sorted(stck)==sorted(s1):        #check first window
            return True
        for right in range(k,len(s2)):      #slide the window
            stck.pop(0)                     #remove leftmost character
            stck.append(s2[right])          #add new character
            if sorted(stck)==sorted(s1):    #check current window
                return True
        return False