class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def sums(left, right):
          return numbers[left] + numbers[right]
        left, right = 0, len(numbers) - 1
        while left < right:
          if sums(left, right) > target:
            right -= 1
          elif sums(left, right) < target:
            left += 1
          else:
            return left, right
solution = Solution()
solution.twoSum([1,2,3,4,5,6,7], 3)

