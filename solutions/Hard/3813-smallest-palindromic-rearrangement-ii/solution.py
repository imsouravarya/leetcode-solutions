import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        
        odd_char = ""
        odd_count = 0
        half_counts = {}
        
        # Determine half-character requirements and check palindrome validity
        for char in sorted(counts.keys()):
            count = counts[char]
            if count % 2 != 0:
                odd_count += 1
                odd_char = char
            half_counts[char] = count // 2
            
        if odd_count > 1:
            return ""
            
        total_half_length = sum(half_counts.values())
        
        # Calculate initial total permutations for the first half
        P_current = math.factorial(total_half_length)
        for cnt in half_counts.values():
            P_current //= math.factorial(cnt)
            
        # If k is larger than the total possible palindromic rearrangements
        if k > P_current:
            return ""

        first_half = []
        
        # Build the first half in O(N * 26) time using O(1) permutation updates
        for pos in range(total_half_length):
            remaining_len = total_half_length - pos
            
            for char in sorted(half_counts.keys()):
                if half_counts[char] > 0:
                    # O(1) formula for permutations if we choose 'char' at this position
                    perms_if_char = P_current * half_counts[char] // remaining_len
                    
                    if k <= perms_if_char:
                        first_half.append(char)
                        half_counts[char] -= 1
                        P_current = perms_if_char  # Update P_current for the next position
                        break
                    else:
                        k -= perms_if_char
                        
        first_half_str = "".join(first_half)
        return first_half_str + odd_char + first_half_str[::-1]