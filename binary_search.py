class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0                         #setting lower bound
        u=len(nums)-1               #setting upper bound
        while l <= u:
            mid = (l+u)//2          # mid value
            if nums[mid]==target:   #checking condition
                return mid
            else:
                if nums[mid]<target:
                    l=mid+1
                else:
                    u=mid-1
        return - 1