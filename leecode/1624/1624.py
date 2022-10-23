from cmath import inf
from re import S


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
      n = [-1]*26
      max_len = -1
      for index, item in enumerate(s):
        alpha = ord(item)-ord('a')
        if n[alpha] < 0:
          n[alpha] = index
        else:
          max_len = max(index - n[alpha], max_len)
      return max(max_len-1,-1)
solution = Solution()
print(solution.maxLengthBetweenEqualCharacters("abca"))