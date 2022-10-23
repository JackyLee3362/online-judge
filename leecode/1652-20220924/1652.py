class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
      n, step =len(code), 1 if k > 0 else -1
      ret = [0 for i in range(n)]
      for i in range(n):
        for j in range(i+step, i+k+step,step):
          ret[i] += code[j % n]
      return ret
solution = Solution()
print(solution.decrypt([5,7,1,4], 3))
print(solution.decrypt([1,2,3,4], 0))   
print(solution.decrypt([2,4,9,3], -2))   
            
            