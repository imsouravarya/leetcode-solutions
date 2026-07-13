# Maximum Sum Subarray of Size K

## 📌 Problem Statement
Given an array of integers `arr` and an integer `k`, find the maximum sum of a subarray of size `k`. 

## 🚀 Approach: Sliding Window Technique
Instead of calculating the sum of every possible subarray from scratch (which would result in an inefficient `O(N*K)` time complexity), this solution uses the **Sliding Window** technique to achieve an optimal `O(N)` solution.

### How it works:
1. **Initialize the Window:** First, calculate the sum of the first `k` elements. This acts as our initial "window".
2. **Slide the Window:** Iterate through the rest of the array from index `k` to the end.
3. **Update the Sum in O(1):** For each step, slide the window forward by subtracting the element that is left behind (`arr[i-k]`) and adding the new element that enters the window (`arr[i]`).
4. **Track the Maximum:** Keep track of the maximum sum encountered during the traversal.

## 💻 Python 3 Solution

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        
        # Edge case: If array size is less than k
        if n < k:
            return -1
            
        # Step 1: Calculate sum of the first 'k' elements
        current_sum = 0
        for i in range(k):
            current_sum += arr[i]
            
        max_sum = current_sum
        
        # Step 2: Slide the window
        for i in range(k, n):
            # Subtract the outgoing element and add the incoming element
            current_sum = current_sum - arr[i-k] + arr[i]
            
            # Update max_sum if the current window's sum is larger
            if current_sum > max_sum:
                max_sum = current_sum
            
        return max_sum
