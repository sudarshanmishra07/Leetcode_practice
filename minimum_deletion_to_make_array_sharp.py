class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deletion = 0
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i]^last==0:
                deletion +=1
            else:
                last=nums[i]
        return deletion

