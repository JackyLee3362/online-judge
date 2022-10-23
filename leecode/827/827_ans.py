class Solution:
    def find(self, p, x): # 查
      if p[x] != x:
        p[x] = self.find(p, p[x])
      return p[x]

    def union(self, p, sz, a, b): # 并
      ra, rb = self.find(p, a), self.find(p, b)
      if ra == rb:
        return
      if sz[ra] > sz[rb]:
        ra, rb = rb, ra
      sz[rb] += sz[ra]
      p[ra] = p[rb]

    def largestIsland(self, grid: list[list[int]]) -> int:
      n, ans = len(grid), 0
      p,sz = [i for i in range(n*n+10)], [1 for i in range(n*n+10)]
      dirs = [[1,0], [-1,0], [0,1], [0,-1]]
      # 构造关系
      for i in range(n):
        for j in range(n):
          if grid[i][j] == 0:
            continue
          for di in dirs:
            x, y = i+di[0], j+di[1]
            if x<0 or x>=n or y<0 or y>=n or grid[x][y] == 0:
              continue
            self.union(p, sz, i*n+j+1, x*n+y+1)
      for i in range(n):
        for j in range(n):
          if grid[i][j] == 1:
            ans = max(ans, sz[self.find(p, i*n+j+1)])
          else:
            tot = 1
            vis = set()
            for di in dirs:
              x, y = i+di[0], j+di[1]
              if x<0 or x>=n or y<0 or y>=n or grid[x][y] == 0:
                continue
              root = self.find(p, x*n+y+1)
              if root in vis:
                continue
              tot += sz[root]
              vis.add(root)
            ans = max(ans, tot)
      return ans
              

solution = Solution()
ans = solution.largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]])
print(ans)