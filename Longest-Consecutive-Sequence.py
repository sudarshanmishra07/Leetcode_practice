nums = [1,2,3,100,101,4,5,6,7]
res = [nums[0]]                     #store the longest sequence
temp = [nums[0]]                    #track current sequence
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        temp.append(nums[i])        #extend consecutive sequence
    else:
        if len(temp) > len(res):
            res = temp              #update longest sequence
        temp = [nums[i]]            #start a new sequence

if len(temp) > len(res):
    res = temp                      #check the last sequence

print(res)
print(len(res))