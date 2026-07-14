# Longest Substring with K Unique Characters

##  Problem Statement
Given a string `s` and an integer `k`, find the length of the longest substring that contains **exactly `k` unique characters**. If no such substring exists, return `-1`.

##  Approach: Variable-Sized Sliding Window with Hash Map
Instead of a brute-force approach that checks every possible substring, this solution uses the **Sliding Window** technique with a hash map (dictionary) to achieve an optimal `O(N)` time complexity.

### How it works:
1. **Expand the Window (Right Pointer `b`):** We slide the right pointer `b` across the string and add each character to a hash map (`char_map`) to keep track of its frequency.
2. **Track Uniques:** The size of the hash map (`len(char_map)`) represents the number of unique characters currently inside our window.
3. **Shrink the Window (Left Pointer `a`):** If the number of unique characters exceeds `k`, we enter a `while` loop to shrink the window from the left. We decrease the frequency of `s[a]` in the map and increment `a`. If a character's frequency hits `0`, we completely remove it from the map.
4. **Update Max Length:** Whenever the hash map has **exactly `k`** unique characters, we calculate the current window length (`b - a + 1`) and update our `max_len`.

##  Python 3 Solution

```python
class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        a = 0  # Left pointer
        max_len = -1  
        char_map = {}  # Dictionary to track unique characters and frequencies
        
        for b in range(len(s)):
            # 1. Expand: Add current character to map
            current_char = s[b]
            char_map[current_char] = char_map.get(current_char, 0) + 1
            
            # 2. Shrink: If uniques exceed k, shrink from left
            while len(char_map) > k:
                left_char = s[a]
                char_map[left_char] -= 1 
                
                if char_map[left_char] == 0:
                    del char_map[left_char]
                    
                a += 1 
            
            # 3. Update Max Length: When uniques are exactly k
            if len(char_map) == k:
                current_length = b - a + 1
                if current_length > max_len:
                    max_len = current_length
                    
        return max_len
