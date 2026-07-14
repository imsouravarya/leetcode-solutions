class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a = 0
        min_len = float('inf')
        current_sum = 0
        b = 0
        for b in range(len(nums)):
            current_sum = current_sum + nums[b]

            while current_sum >= target:
                current_length = b - a + 1
                if current_length < min_len:
                    min_len = current_length

                current_sum = current_sum - nums[a]
                a += 1


        if min_len == float('inf'):
            return 0

        else:
            return min_len


