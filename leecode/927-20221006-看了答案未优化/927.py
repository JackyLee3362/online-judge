from collections import Counter

class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
      s = sum(arr)
      if s % 3:
        return [-1,-1]
      if s == 0:
        return [0,2]
      partial = s // 3
      a,b,c = partial,2*partial,3*partial
      pa,pb,pc = 0,0,0
      for index,item in enumerate(arr):
        if item == 1:
          a,b,c = a-1,b-1,c-1
        else:
          continue
        if a == 0:
          pa = index
        elif b == 0:
          pb = index
        elif c == 0:
          pc = index
      print(pa,pb,pc)
      na,nb,nc = arr[0:pa+1],arr[pa+1:pb+1],arr[pb+1:pc+1]
      print("list",na,nb,nc)
      while True:
        if na[0] == 0:
          na.pop(0)
        else:
          break
      while True:
        if nb[0] == 0:
          nb.pop(0)
        else:
          break
      while True:
        if nc[0] == 0:
          nc.pop(0)
        else:
          break
      if na == nb == nc:
        return [pa+1,pb+1]
        

solution = Solution()
# print(solution.threeEqualParts([1,0,1,0,1,0,1,0,1,0,1]))
print(solution.threeEqualParts([1,0,1,0,1]))
          
      
