class Solution:
    def maxSubarraySum(self, arr, k): 
        n = len(arr)
        if n < k:
                print("Invalid")
                return -1
        window_sum = sum(arr[:k])                            #calculate sum of first window
        max_sum = window_sum
        for i in range(n - k):                                #slide the window through remaining array
                window_sum = window_sum - arr[i] + arr[i + k] #remove outgoing element add incoming element
                max_sum = max(window_sum, max_sum)            #update maximum sum
        return max_sum
