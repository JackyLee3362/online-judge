class Solution:
    def Knapsack(self, w: list[int], v: list[int], t: int) -> int:
      n = len(w) # 物品总数
      w.insert(0, 0)
      v.insert(0, 0)
      dp = [[0 for i in range(t+1)] for j in range(n+1)] # (n+1, t+1)
      for i in range(1, n+1): # i in [1,2,...,n]
        for j in range(t, 0, -1): # j in [1,2,...,t]
          if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
          else:
            dp[i][j] = dp[i-1][j]
      return dp
dp = Solution().Knapsack([2,3,4,5], [3,4,5,6], 8)
for i in dp:
  print(i)
