class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                                 #taking sorted list
        i = 0
        result = []
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:    #skip duplicate values for first element
                i += 1
                continue
            if nums[i] > 0:
                break
            l = i + 1                               #left pointer
            r = len(nums) - 1                       #right pointer
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1                                  #move left pointer
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1                                  #move right pointer
                    l += 1                          #move both pointer after finding a triplet
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
            i += 1                                  #move to next first element
        return result