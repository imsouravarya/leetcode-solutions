class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        a = 0  
        max_len = -1  
        char_map = {}  
        
        
        for b in range(len(s)):
            
            current_char = s[b]
            char_map[current_char] = char_map.get(current_char, 0) + 1
            
           
            while len(char_map) > k:
                left_char = s[a]
                char_map[left_char] -= 1 
                
                
                if char_map[left_char] == 0:
                    del char_map[left_char]
                    
                a += 1 
            
            
            if len(char_map) == k:
                current_length = b - a + 1
                if current_length > max_len:
                    max_len = current_length
                    
        return max_len
