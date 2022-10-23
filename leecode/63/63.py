class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
      m,n = len(obstacleGrid),len(obstacleGrid[0])
      dp = [[0]*n for i in range(m)]
      for i in range(m):
        for j in range(n):
          if not obstacleGrid[i][j]:
            if i == j == 0:
              dp[i][j] = 1
            else:
              dp[i][j] = dp[i-1][j] + dp[i][j-1]
      print(dp)
      return dp[-1][-1]

solution = Solution()
ans = solution.uniquePathsWithObstacles([[0,0],[0,1],[0,0]])
print(ans)