class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
      first, second = 0,0
      if s1 == s2:
        return True
      n = len(s1)
      cnt =  0
      for i in range(n):
        if s1[i] != s2[i]:
          cnt += 1
          if cnt == 1:
            first = i
          elif cnt == 2:
            second = i
          elif cnt > 2:
            return False
      if s1[first] == s2[second] and s1[second] == s2[first]:
        return True
      return False
      
      
solution = Solution()
print(solution.areAlmostEqual("bank", "kanb"))
        

