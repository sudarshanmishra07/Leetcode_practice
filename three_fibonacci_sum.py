class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a=0
        b=1
        c=1
        while a+b+c<n:
            a,b,c = b,c,b+c
        
        return a+b+c==n