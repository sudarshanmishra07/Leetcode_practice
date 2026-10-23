class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}                                  #store frequency of each character
        res = 0                                     #store maximum window length
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)     #count current character
            while (r-l+1) - max(count.values())>k:  
                count[s[l]]-=1                      #remove left character
                l+=1                                #move left pointer
            res = max(res,r-l+1)                    #update maximum valid length
        return res