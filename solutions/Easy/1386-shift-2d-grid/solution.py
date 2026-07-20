from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])
        

        flat_list = []
        for row in grid:
            flat_list.extend(row)
            

        k = k % len(flat_list)
        

        if k != 0:

            flat_list = flat_list[-k:] + flat_list[:-k]
            

        result = []
        for i in range(0, len(flat_list), n):

            result.append(flat_list[i : i + n])
            
        return result