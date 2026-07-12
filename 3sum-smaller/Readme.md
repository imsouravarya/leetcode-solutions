# Triplets with Smaller Sum (3Sum Smaller)

## Problem Statement
Given an array `arr` of distinct integers and a target value `k`. The task is to find the count of triplets `(arr[i], arr[j], arr[k])` such that `i < j < k` and `arr[i] + arr[j] + arr[k] < k`.

**Example:**
- **Input:** `arr = [-2, 0, 1, 3]`, `k = 2`
- **Output:** `2`
- **Explanation:** Below are the valid triplets: 
  1. `(-2, 0, 1)` -> Sum = -1 (< 2)
  2. `(-2, 0, 3)` -> Sum = 1 (< 2)

## Approach: Sorting + Two Pointers
This problem is an excellent variation of the classic 3Sum problem. We can solve it efficiently by avoiding nested loops for all three numbers.

1. **Sort the Array:** Sorting is essential for the two-pointer technique to work.
2. **Anchor one pointer (`i`):** Iterate through the array, fixing the first element `arr[i]`.
3. **Set Two Pointers (`a` and `b`):** Place the left pointer `a` right after `i` (`a = i + 1`) and the right pointer `b` at the end of the array (`b = n - 1`).
4. **The "Difference" Trick:**
   - Calculate the sum: `current_sum = arr[i] + arr[a] + arr[b]`
   - If `current_sum < k`, it means `arr[b]` is valid. Because the array is sorted, any number between `a` and `b` replacing `arr[b]` will also result in a sum strictly less than `k`.
   - Therefore, instead of counting one by one, we can directly add `(b - a)` to our count and move the left pointer forward (`a++`).
   - If `current_sum >= k`, the sum is too large, so we decrement the right pointer (`b--`).

## Complexity Analysis
- **Time Complexity:** `O(N^2)` 
  - Sorting the array takes `O(N log N)`. 
  - The nested loops (one `for` and one `while`) take `O(N^2)` in the worst case. Overall time complexity is dominated by `O(N^2)`.
- **Space Complexity:** `O(1)` (excluding the internal space required for sorting), as we are only using a few constant extra variables.