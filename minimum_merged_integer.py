class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        merged=[]                           #store all merged integer value
        res = 0                             #store result
        if len(nums)<=1:
            return nums                     #return nums if it has 0 or 1 element
        for i in range(0, len(nums)-1,2):   #iterate 
            value=str(nums[i])+str(nums[i+1])   #covert nums into string and concatenate them
            merged.append(int(value))           #convert merged string into integer
        res = min(merged)                   #minimum value from merged
        return res