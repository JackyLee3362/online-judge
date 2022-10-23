from collections import Counter
# from typing import List
# import time
# try1
# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:
#       ans = '0'
#       for i in range(1,n):
#         temp = ''
#         for j in ans:
#           if j == '0':
#             temp += '01'
#           else:
#             temp += '10'
#         ans = temp
#       return ans[k]
# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:
#       ans = [0,1,1,0,1,0,0,1]
#       while n > 3:
#         d = pow(2, n-3)
#         if k <= d:
#           n -= 2
#         elif k <= d * 2:
#           n -= 1
#         elif k <= d * 3:
#           n -= 1
#           k -= d
#         else:
#           n -= 2
#           k -= d * 3

#       return ans[k-1]
      
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k += 2**(n-1) - 1
        ans = 0
        while k > 1:
            if k % 2:
                ans += 1
            k //= 2
        return ans % 2 

solution = Solution()

ans = '0110100110010110'
n = 5
k = 6
for k in range(1,16):
  print(solution.kthGrammar(n,k),"ans is", ans[k-1])
# print(solution.kthGrammar(4,3))
# print(solution.kthGrammar(30,434991989))
