class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)                                            #find length of array
        if n < k:
                print("Invalid")                                
                return -1
        window_sum = sum(arr[:k])                               #calculate the sum of first k element
        max_sum = window_sum
        for i in range(n - k):                                  #slide the window 
                window_sum = window_sum - arr[i] + arr[i + k]   #remove the leftmost element and add next element
                max_sum = max(window_sum, max_sum)              # maximum sum
        return max_sum
