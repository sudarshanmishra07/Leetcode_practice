class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)
        if n < k:
                print("Invalid")
                return -1
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(n - k):
                window_sum = window_sum - arr[i] + arr[i + k]
                max_sum = max(window_sum, max_sum)
        return max_sum
