class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        

        zero_blocks = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_blocks.append(j - i)
                i = j
            else:
                i += 1
        
  
        max_gain = 0
        for k in range(len(zero_blocks) - 1):
            max_gain = max(max_gain, zero_blocks[k] + zero_blocks[k + 1])
            
        return total_ones + max_gain