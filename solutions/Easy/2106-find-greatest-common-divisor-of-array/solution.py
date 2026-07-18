class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)

        return math.gcd(minn, maxx)