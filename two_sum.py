def two_sum(nums, target):
  i = 0
  while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return[i,j]
                break
            j += 1
        i += 1
nums=[2,7,11,15]
target=26
print(two_sum(nums,target))
            
