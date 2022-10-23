from itertools import permutations


class Solution:
    def distinctSubseqII(self, s: str) -> int:
      n = len(s)
      alpha = [-1] * 26 # 记录26个字母最后一次出现的位置
      dp = [[0]*n for i in range(n)]
      # 初始化第一行
      dp[0][0] = 1
      first_alpha_pos = ord(s[0]) - 97
      alpha[first_alpha_pos] = 0
      # 完成剩余表格
      for i in range(1, n):
        pos = ord(s[i]) - 97 # 找到哈希表中对应字母的位置
        val = alpha[pos]
        if val < 0:
          # 说明从来没有出现过
          dp[i][i] = 1
          alpha[pos] = i
          for j in range(0,i):
            dp[i][j] = dp[i-1][j]*2
        else:
          for j in range(i):
            if j >= val: # 不相等
              dp[i][j] = 2 * dp[i-1][j]
            else: # 相等
              dp[i][j] = 2 * dp[i-1][j] - dp[val-1][j]
        alpha[pos] = i # 记录最后出现过的
      # print(s, "ans is ", sum(dp[-1]))
      # print("alpha", alpha)
      return dp
solution = Solution()
print(solution.distinctSubseqII("ab"))
print(solution.distinctSubseqII("aba"))
print(solution.distinctSubseqII("abcb"))
print(solution.distinctSubseqII("aaa"))