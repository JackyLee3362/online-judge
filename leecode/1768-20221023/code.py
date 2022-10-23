from collections import Counter
from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        ans = ""
        if n1 >= n2:
            for i in range(n2):
                ans += word1[i] + word2[i]
            ans += word1[i+1:]
        else:
            for i in range(n1):
                ans += word1[i] + word2[i]
            ans += word2[i+1:]
        return ans
solution = Solution()
print(solution.mergeAlternately(word1 = "abc", word2 = "pqr"), "ans is apbqcr")
print(solution.mergeAlternately(word1 = "ab", word2 = "pqrs"), "ans is apbqrs")
