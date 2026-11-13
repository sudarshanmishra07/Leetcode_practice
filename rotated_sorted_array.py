class Solution:
    def findMin(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:                  #continue until both pointer meet
            mid = (l+r)//2          #find middle index
            if nums[mid]>nums[r]:   #if minimum in right half
                l = mid+1           #move left pointer
            else:
                r = mid             #move right pointer to mid
        return nums[l]