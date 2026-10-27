class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        total = sum(nums)                           #sum of all original numbers
        max_arr=[]                                  # store possible gains from rearranging each digits
        for num in nums:
            digitized_sort = int(''.join(sorted(str(num),reverse=True)))    #convert number to string, sort digits join them convert result to integer
            max_arr.append(digitized_sort-num)
        max_arr.sort(reverse=True)                  # sort gains in desc order
        for gain in max_arr[:k]:                    # select largest gain add to original sum
            total +=gain
        return total                                # return maximum sum
            
            