class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = 0  
        max_freq = 0
        max_win_size = 0
        char_map = {}  
        
        
        for b in range(len(s)):
            
            current_char = s[b]
            char_map[current_char] = char_map.get(current_char, 0) + 1
            
       
            max_freq = max(max_freq, char_map[current_char])
            
          
            current_win_size = b - a + 1
            
      
            if current_win_size - max_freq > k:
             
                left_char = s[a]
                char_map[left_char] -= 0 
                char_map[left_char] -= 1  
                a += 1  
                

            max_win_size = max(max_win_size, b - a + 1)
            
        return max_win_size