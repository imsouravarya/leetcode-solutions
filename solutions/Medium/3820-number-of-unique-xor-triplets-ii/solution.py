class Solution:

    def uniqueXorTriplets(self, nums: list[int]) -> int:

        max_val = max(nums)

        limit = 1 << (max_val.bit_length())


        st = [False] * limit
        for a in nums:
            for b in nums:
                st[a ^ b] = True


        s = [False] * limit
        for ab in range(limit):
            if st[ab]:
                for c in nums:
                    s[ab ^ c] = True


        return sum(s)