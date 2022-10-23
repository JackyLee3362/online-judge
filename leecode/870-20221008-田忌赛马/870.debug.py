class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
      n = len(nums1)
      ids = sorted(range(n), key=lambda i: nums2[i])
      print(f"ids is {ids}")
      print(nums2)
      for index,item in enumerate(nums2):
        nums2[index] = (item, index)
      print(nums2)
      nums2.sort(key=lambda items:items[0])
      print("after sorting",nums2)
      nums1.sort()
      sum_i = 0
      max_k = 0
      for k in range(n):
        temp_sum = 0
        for i in range(n):
          if nums1[(i+k)%n] > nums2[i][0]:
            temp_sum += 1
        if temp_sum >= sum_i:
          sum_i = temp_sum
          max_k = k
          print(f"k is {k}, temp_sum is {temp_sum}")
        else:
          break
      print(f"when break, max_k is {max_k}")
      print(f"nums1 is", nums1)
      temp_ans = nums1[max_k:] + nums1[:max_k]
      print(f"after rotate, nums1 is", temp_ans)
      ans = [0] * n
      for i in range(n):
        j = nums2[i][1]
        ans[j] = temp_ans[i]
      print(f"ans is {ans}.")
      return ans
solution = Solution()

print(solution.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))
# print(solution.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))