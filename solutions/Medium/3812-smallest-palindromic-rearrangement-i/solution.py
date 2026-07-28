from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = Counter(s)
        
        first_half = []
        middle = ""
        
        for char in sorted(counts.keys()):
            if counts[char] % 2 != 0:
                middle = char
            first_half.append(char * (counts[char] // 2))
        
        half_str = "".join(first_half)
        return half_str + middle + half_str[::-1]