nums=[1,2,3,4]
res=[1]*(len(nums))
prefix=1                            #store the product of all elements to the left
for i in range(len(nums)):          #calculate prefix products
    res[i]=prefix
    prefix*=nums[i]
postfix=1                           #store the product of all elements to the right
for i in range(len(nums)-1,-1,-1):  #calculating postfix products and multiply with prefix products
    res[i]*=postfix
    postfix*=nums[i]
print(res)


