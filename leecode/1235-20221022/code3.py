from bisect import bisect_right
from collections import Counter
from operator import itemgetter
from typing import List
import time

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=itemgetter(1))
        dp = [0] * (n+1)
        for i in range(1,n+1):
            k = bisect_right(jobs, jobs[i-1][0], hi=i, key=itemgetter(1))
            dp[i] = max(dp[i-1], dp[k]+jobs[i-1][2])
        return dp[n]
solution = Solution()
print(solution.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]), "ans is 120")
print(solution.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]), "ans is 150")
print(solution.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]), "ans is 6")
print(solution.jobScheduling([6,15,7,11,1,3,16,2],[19,18,19,16,10,8,19,8],[2,9,1,19,5,7,3,19]), "ans is 41")



