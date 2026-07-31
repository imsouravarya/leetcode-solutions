from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:

        counts = Counter(word)
  
        freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        

        for i, count in enumerate(freqs):

            pushes = (i // 8) + 1
            total_pushes += count * pushes
            
        return total_pushes