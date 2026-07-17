class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum = sum(nums[:k])
        max_sum = current_sum
        a = 0
        for b in range(k, len(nums)):
            current_sum = current_sum - nums[a] + nums[b]
            a += 1

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum/k
        
        