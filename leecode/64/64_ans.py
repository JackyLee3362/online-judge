class Solution:
    def minPathSum(self, grid):
        dp = [float('inf')] * (len(grid[0])+1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]
solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))




