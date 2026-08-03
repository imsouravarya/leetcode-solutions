class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        from functools import cache
import math
from typing import List


class Solution:

  def stoneGameIII(self, stoneValue: List[int]) -> str:
    n = len(stoneValue)

    @cache
    def dp(i: int) -> int:
      # Base case: no stones left
      if i == n:
        return 0

      res = -math.inf
      summ = 0

      # A player can take 1, 2, or 3 stones
      for j in range(i, min(i + 3, n)):
        summ += stoneValue[j]
        # Maximize current score minus opponent's optimal score from next index
        res = max(res, summ - dp(j + 1))

      return res

    score = dp(0)

    if score > 0:
      return "Alice"
    elif score < 0:
      return "Bob"
    else:
      return "Tie"