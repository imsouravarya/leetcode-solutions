class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.rstrip().rsplit(' ', 1)[-1]
        ans = len(last_word)
        return ans
        