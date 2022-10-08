from curses.ascii import NUL
from requests import NullHandler


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split()
        ans = ""
        return " ".join(s.split(" ")[::-1])[::-1]
solution = Solution()
s = "Let's take LeetCode contest"
ans = solution.reverseWords(s)
print(ans)
