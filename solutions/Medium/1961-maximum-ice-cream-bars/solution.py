class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for i in costs:
            if coins >= i:
                coins = coins - i
                count = count + 1
            else:
                break
        return count
    


        

        