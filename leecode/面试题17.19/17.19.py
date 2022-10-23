class Solution:
    def missingTwo(self, nums: list[int]) -> list[int]:
      n = len(nums) + 2
      sigma = n * (n+1) // 2
      total = sum(nums)
      delta = sigma - total
      mid = delta // 2
      sigma_mid = mid * (mid+1) // 2
      total_ = 0
      for i in nums:
        if i > mid:
          continue
        total_ += i
      ans_1 = sigma_mid - total_
      return [ans_1, delta - ans_1 ]
solution = Solution()
print(solution.missingTwo([1]))
      
      
      