import heapq
# https://docs.python.org/zh-cn/3/library/heapq.html


class Solution:
    def getKthMdpgicNumber(self, k: int) -> int:
        nums = [3, 5, 7]
        q, vis = [1], set([1])

        while q:
            t = heapq.heappop(q)
            k -= 1
            if not k:
                return t
            for x in nums:
                if x*t not in vis:
                    heapq.heappush(q, t*x)
                    vis.add(t*x)
        return -1


print(Solution().getKthMdpgicNumber(251))
