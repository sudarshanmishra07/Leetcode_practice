class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1                             #minimum possible speed
        r=max(piles)                    #maximum possible speed
        res=r
        while l<=r:
            k = (l+r)//2                #finding middle
            hours=0
            for p in piles:
                hours += math.ceil(p/k) #calculating hours

            if hours<=h:
                res = min(res,k)        #store minimum valid speed
                r = k-1
            else:
                l = k+1
        return res                      #return minimum valid speed