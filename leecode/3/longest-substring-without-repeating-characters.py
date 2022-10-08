class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      last = [-1] * 128
      length = len(s)
      start = 0
      res = 0
      for i in range(length):
        index = ord(s[i])
        start = max(start, last[index] + 1)
        res = max(res, i - start + 1)
        last[index] = i
      return res

solution = Solution()
m = solution.lengthOfLongestSubstring('pwwkew')
print(m)

          