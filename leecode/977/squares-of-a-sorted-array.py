class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
          while i < j:
              nums[i], nums[j] = nums[j], nums[i]
              i += 1
              j -= 1
        l = len(nums) 
        k = k % l
        reverse(0, l - 1)
        reverse(0, k - 1)
        reverse(k, l - 1)
        
    
solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3)
