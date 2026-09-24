nums = [1,2,3,100,101,4,5,6,7]
res = [nums[0]]
temp = [nums[0]]
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        temp.append(nums[i])
    else:
        if len(temp) > len(res):
            res = temp
        temp = [nums[i]]

if len(temp) > len(res):
    res = temp

print(res)
print(len(res))