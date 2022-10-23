class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        length = len(nums)
        while right < length:
          if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
          right += 1
        while left < length:
          nums[left] = 0
          left += 1
        return nums
solution = Solution()
nums = solution.moveZeroes([0])
print(nums)
