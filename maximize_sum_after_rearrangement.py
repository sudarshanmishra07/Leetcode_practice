class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        max_arr=[]
        for num in nums:
            digitized_sort = int(''.join(sorted(str(num),reverse=True)))
            max_arr.append(digitized_sort-num)
        max_arr.sort(reverse=True)
        for gain in max_arr[:k]:
            total +=gain
        return total
            
            