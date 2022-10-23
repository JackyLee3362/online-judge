class Solution:
    def scoreOfParentheses(self, s: str) -> int:
      def dfs(sub):
        if sub == "()":
          return 1
        cnt,n = 0,len(sub)
        for i,c in enumerate(sub):
          if c == '(': cnt+=1
          else: cnt -= 1
          if cnt == 0:
            break
        if i == 1:
          return 1+dfs(sub[2:])
        elif i == n-1:
          return 2 * dfs(sub[1:-1])
        else:
          return dfs(sub[0:i+1]) + dfs(sub[i+1:])
      return dfs(s)
def test_solution():
  solution = Solution()
  assert solution.scoreOfParentheses("()") == 1
  assert solution.scoreOfParentheses("(())") == 2
  assert solution.scoreOfParentheses("()()") == 2
  assert solution.scoreOfParentheses("(()(()))") == 6
