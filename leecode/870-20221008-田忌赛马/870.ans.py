class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        ans = [0] * n
        nums1.sort()
        ids = sorted(range(n), key=lambda i: nums2[i])
        left, right = 0, n - 1
        for x in nums1:
            if x > nums2[ids[left]]:
                ans[ids[left]] = x  # 用下等马比下等马
                left += 1
            else:
                ans[ids[right]] = x  # 用下等马比上等马
                right -= 1
        return ans
solution = Solution()
print(solution.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))
