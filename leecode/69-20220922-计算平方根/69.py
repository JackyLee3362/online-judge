class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, 46400
        while 1:
            if low + 1 >= high:
                return low
            mid = (low + high) // 2
            if x > mid ** 2:
                low = mid
            elif x < mid ** 2:
                high = mid
            else:
                return mid


solution = Solution()
print(solution.mySqrt(2147395600))
