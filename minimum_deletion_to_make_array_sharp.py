class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deletion = 0                    #count deletions
        last = nums[0]                  #store the last kept element
        for i in range(1,len(nums)):
            if nums[i]^last==0:         # XOR is 0 when both numbers equal
                deletion +=1            #delete the duplicate number
            else:
                last=nums[i]            #update last kept element
        return deletion                 #return total deletions

