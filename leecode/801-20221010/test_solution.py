from cmath import inf


List = list
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
      n = len(nums1)
      dp = [[inf,inf] for _ in range(n)]
      dp[0] = [0,1]
      for i in range(1,n):
        if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
          dp[i][0] = dp[i-1][0]
          dp[i][1] = dp[i-1][1] + 1
        if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
          dp[i][0] = min(dp[i][0],dp[i-1][1])
          dp[i][1] = min(dp[i][1],dp[i-1][0]+1)
      # print(dp)
      return min(dp[-1])
solution = Solution()
print(solution.minSwap([0,4,4,5,9],[0,1,6,8,10]))

def test_solution():
  assert solution.minSwap([1,2,3,8],[5,6,7,4]) == 2,"fail"
  assert solution.minSwap([1,3,5,4],[1,2,3,7])== 1
  assert solution.minSwap([0,3,5,8,9],[2,1,4,6,9])== 1
  assert solution.minSwap([4,2,3,5],[1,6,7,8])== 1
  # 79/117
  assert solution.minSwap([0,4,4,5,9],[0,1,6,8,10]) == 1