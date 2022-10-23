
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
          return 1
        elif n == 1:
          return 2
        elif n == 2:
          return 3 if presses == 1 else 4
        elif n >= 3:
          if presses == 1:
            return 4
          return 7 if presses == 2 else 8
          
          


solution = Solution()
print(solution.flipLights(2, 1))
      

      