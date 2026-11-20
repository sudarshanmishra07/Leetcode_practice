def two_sum(nums, target):
  i = 0
  while i < len(nums):
        j = i + 1                           #start second pointer from next index
        while j < len(nums):                #check remaining elements
            if nums[i] + nums[j] == target: #check if pair sum=target
                return[i,j]                 #return indices of two numbers
                break                       
            j += 1                          #move second pointer forward
        i += 1                              #move first pointer forward

            
