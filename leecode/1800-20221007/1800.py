class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
      max_sum = temp_sum = nums[0]
      n = len(nums)
      for i in range(1,n):
        if nums[i] > nums[i-1]:
          temp_sum += nums[i]
        else:
          max_sum = max(max_sum, temp_sum)
          temp_sum = nums[i]
        
      return max(max_sum, temp_sum)
solution = Solution()

print(solution.maxAscendingSum([10,20,30,5,10,50]))
print(solution.maxAscendingSum([10,20,30,40,50]))
print(solution.maxAscendingSum([12,17,15,13,10,11,12]))
print(solution.maxAscendingSum([100,10,1]))