class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0                        #store maximum length found
        hashset = set()                       #store unique character in the window
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])          #remove character until s[r] is unique
                l+=1
            hashset.add(s[r])                 #add current character
            max_length = max(max_length,r-l+1)#update max length
        return max_length