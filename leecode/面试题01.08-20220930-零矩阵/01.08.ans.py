class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        row, col =[0]*m, [0]*n
        for i in range(m):
          for j in range(n):
            if not matrix[i][j]:
              row[i] = col[j] = 1
        for i in range(m):
          for j in range(n):
            if row[i] or col[j]:
              matrix[i][j] = 0
solution = Solution()
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
solution.setZeroes(matrix)
print(matrix)