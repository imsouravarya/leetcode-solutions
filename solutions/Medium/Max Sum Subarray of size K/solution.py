class Solution
    def maxSubarraySum(self, arr, k)
        # code here 
        n = len(arr)
        
        if n  k
            return -1
            
        
        current_sum = 0
        for i in range(k)
            current_sum += arr[i]
            
        max_sum = current_sum
        
        for i in range(k, n)
            current_sum = current_sum - arr[i-k] + arr[i]
            
            
            
            if current_sum  max_sum
                max_sum = current_sum
            
        return max_sum
            
             
             
            
