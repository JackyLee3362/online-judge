class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
      
      m ,n= len(grid),len(grid[0])
      G = []
      Empty = set()
      index = 0
      visited = [[0]*n for i in range(m)]
      
      def dfs(i, j, index):
        if i<0 or j<0 or i>m-1 or j>n-1: # 如果超出范围，退出
          return
        elif visited[i][j] == 1: # 如果已经访问过，则退出
          return
        elif grid[i][j] == 0:
          # (i,j) 加入g"周围空点"集合
          G[index][1].add((i,j))
          Empty.add((i,j))
          return
        pass # (i,j) 加入g"占位"集合
        G[index][0].add((i,j))
        visited[i][j] = 1
        dfs(i,j-1,index)
        dfs(i+1,j,index)
        dfs(i,j+1,index)
        dfs(i-1,j,index)
      for i in range(m):
        for j in range(n):
          if grid[i][j] == 1 and visited[i][j] == 0:
            G.append([set(),set()])
            dfs(i,j,index)
            index += 1
      # debug
      # for i in range(len(G)):
      #   print(f" full points{i}:", G[i][0])
      #   print(f"full points' number is ", len(G[i][0]))
      #   print(f"empty points{i}:", G[i][1])  
      
      if len(G) == 1:
        return min(len(G[0][0]) + 1, m*n)
      elif len(G) == 0:
        return 1
      ans = 0
      for i in Empty:
        tmp = 0
        for j in range(len(G)):
          if i in G[j][1]:
            tmp += len(G[j][0])
        ans = max(tmp+1, ans)
      # for i in range(len(G)):
      #   for j in range(i+1, len(G)):
      #     if not G[i][1].intersection(G[j][1]) == set():
      #       ans = max(ans, len(G[i][0])+len(G[j][0])+1)
      print("ans is ", ans)
      print("----")
      return ans
solution = Solution()
solution.largestIsland([[1, 0], [0, 1]])
solution.largestIsland([[1,0,0],[0,1,1],[0,0,1]])
solution.largestIsland([[1,1],[1,0]])
solution.largestIsland([[0,0],[0,0]])
solution.largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]])
