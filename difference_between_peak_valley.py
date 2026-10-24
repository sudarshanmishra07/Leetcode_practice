class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak_stck = []
        valley_stck = []
        if len(nums)<3:
            return 0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                peak_stck.append(nums[i])
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                valley_stck.append(nums[i])
        sum_peak = sum(peak_stck)
        sum_valley = sum(valley_stck)
        difference =sum_peak - sum_valley
        return difference
        