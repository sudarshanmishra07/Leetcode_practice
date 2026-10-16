class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l=0                                 #left = buy
        r=1                                 #right= sell
        maxp=0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit= prices[r]-prices[l] #profit = sell - buy
                maxp= max(maxp,profit)      #maximum price
            else:
                l=r                         #move left pointer to r
            r+=1
        return maxp                         #return result