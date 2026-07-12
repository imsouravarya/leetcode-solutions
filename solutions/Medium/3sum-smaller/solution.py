class Solution:
    def countTriplets(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        
        
        if n < 3:
            return 0
            
        arr.sort()
        count = 0    
        
        
        for i in range(n - 2):
            a = i + 1
            b = n - 1
            
            while a < b:
                current_sum = arr[i] + arr[a] + arr[b]
                
                if current_sum < k:
                    
                    
                    count += (b - a)
                    a += 1
                else:
                    
                    b -= 1
                    
        return count
