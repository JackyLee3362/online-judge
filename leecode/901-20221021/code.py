from collections import Counter
from typing import List
from cmath import inf

class StockSpanner:

    def __init__(self):
        self.nums = [[inf,0]]
        
    def next(self, price: int) -> int:
        n = len(self.nums)
        i = len(self.nums) - 1
        while price >= self.nums[i][0]:
            i = self.nums[i][1]
        self.nums.append([price, i])
        return n - i



# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
test = [100, 80, 60, 70, 60, 75, 85]
for price in test:
    print(obj.next(price))