class Solution:
    def specialArray(self, nums: list[int]) -> int:
      counts = [0] * 1001
      for num in nums:
        counts[num] += 1
      sum = len(nums) # 定义
      for index,count in enumerate(counts):
        if sum and sum == index:
          return sum
        sum -= count
      return -1
solution = Solution()
print(solution.specialArray([3,6,7,7,0]))
