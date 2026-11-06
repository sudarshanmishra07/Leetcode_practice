class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak_stck = []                                      #store all peak elements
        valley_stck = []                                    #store all valley elements
        if len(nums)<3:
            return 0
        for i in range(1,len(nums)-1):                      #traverse array excluding first and last elements
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:     #check if current element greater then both adjacent elements
                peak_stck.append(nums[i])                   #add peak to list
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:   #check if current element less then both adjacent elements
                valley_stck.append(nums[i])                 #add valley to list
        sum_peak = sum(peak_stck)                       #calculate sum of all peak
        sum_valley = sum(valley_stck)                   #calculate sum of all valley
        difference =sum_peak - sum_valley               #difference btw peak sum and valley sum
        return difference
        