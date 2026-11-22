class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:                             #continue while search is valid
            mid = (l+r)//2
            if nums[mid]==target:
                return mid                      #if mid = target return mid
            if nums[l]<=nums[mid]:              #check if left half is sorted
                if nums[l]<=target<nums[mid]:   #check if target in left sorted half
                    r = mid-1                   #find in left half                
                else:
                     l = mid+1                  #find in right half
            else:
                if nums[mid]<target<=nums[r]:   #check if target in right sorted half
                    l=mid+1                     #find in right half
                else:
                    r=mid-1                     #find in left half  
        return -1