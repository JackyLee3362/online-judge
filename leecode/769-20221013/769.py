List = list
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
      n = len(arr)
      ans, maxv = 0, 0
      for i in range(n):
        maxv = max(maxv, arr[i])
        if maxv == i:
          ans += 1
      return ans

solution = Solution()
print(solution.maxChunksToSorted([4,3,2,1,0]),"ans is 1") # ans = 1
print(solution.maxChunksToSorted([1,0,2,3,4]),"ans is 4") # ans = 4
print(solution.maxChunksToSorted([1,2,0,3]),"ans is 2") # ans = 2
print(solution.maxChunksToSorted([0,4,5,2,1,3]),"ans is 2") # ans = 2
print(solution.maxChunksToSorted([2,0,1]),"ans is 1") # ans = 1
print(solution.maxChunksToSorted([0,1,3,2]),"ans is 3") # ans = 3