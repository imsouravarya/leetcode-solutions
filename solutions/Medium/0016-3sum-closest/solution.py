class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n-2):
            a = i + 1
            b = n - 1

            while a < b:
                current_sum = nums[i] + nums[a] + nums[b]

                if current_sum == target:
                    return current_sum
                

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
             
                if current_sum < target:
                    a += 1
                else:
                    b -= 1
                    
        return closest
        