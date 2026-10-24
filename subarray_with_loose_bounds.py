class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        stck = []
        count = 0
        for i in range(len(nums)):
            if nums[i]>=minK and nums[i]<=maxK: #check condition
                stck.append(nums[i])            #append to stack
            else:
                n = len(stck)
                count+=n*(n+1)//2               #count subarray present before invalid no.
                stck = []
        n = len(stck)
        count+=n*(n+1)//2                       #count total subarray
        return count