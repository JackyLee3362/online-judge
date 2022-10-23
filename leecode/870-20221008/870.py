class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
      n = len(nums1)
      for index,item in enumerate(nums2):
        nums2[index] = (item, index)
      nums1.sort()
      nums2.sort(key=lambda items:items[0])
      sum_i,max_k,ans = 0,0,[0]*n
      for k in range(n):
        temp_sum = 0
        for i in range(n):
          if nums1[(i+k)%n] > nums2[i][0]:
            temp_sum += 1
        if temp_sum < sum_i:
          break
        sum_i = temp_sum
        max_k = k
      nums1 = nums1[max_k:] + nums1[:max_k]
      for i in range(n):
        ans[nums2[i][1]] = nums1[i]
      return ans
solution = Solution()

print(solution.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))
# print(solution.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))