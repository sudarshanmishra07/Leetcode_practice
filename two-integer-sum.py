class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum = 0
        l=0                                 #left pointer
        r=len(numbers)-1                    #right pointer
        while l < r:
            sum = numbers[l] + numbers[r]   #calculate current sum
            if sum==target:
                return [l+1,r+1]            #return 1 based indices
            if sum > target:
                r-=1                        #decrease sum by moving right pointer left
            if sum < target:
                l+=1                        #increase sum by moving left pointer right
        return                              #return