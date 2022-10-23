class Solution:
    def trimMean(self, arr: list[int]) -> float:
      n = len(arr)
      pn = int(n / 20)
      arr.sort()
      arr2 = arr[pn:-pn]
      return sum(arr2) / len(arr2)
solution = Solution()
print(solution.trimMean(arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
