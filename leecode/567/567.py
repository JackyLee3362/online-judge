class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      if len(s1) > len(s2):
          return False
      index1 = [0] * 26
      index2 = [0] * 26
      for i in range(len(s1)):
        index1[ord(s1[i]) - ord('a')] += 1
        index2[ord(s2[i]) - ord('a')] += 1
      window_size = len(s1)
      for i in range(len(s1), len(s2)):
        if index1 == index2:
          return True
        index2[ord(s2[i-window_size]) - ord('a')] -= 1
        index2[ord(s2[i]) - ord('a') ] += 1
      return index1 == index2


solution = Solution()
isTrue = solution.checkInclusion('adc', 'dcda')
print(isTrue)
