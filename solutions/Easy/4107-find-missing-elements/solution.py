class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        a = sorted_nums[0]
        b = sorted_nums[-1]
        missing = list(set(range(a, b + 1)) - set(sorted_nums))
        lol = sorted(missing)
        return lol



        