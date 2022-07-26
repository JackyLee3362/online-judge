#include <iostream>

class Solution
{
public:
  int climbStairs(int n)
  {
    if (n <= 2)
      return n;
    int dp[46];
    dp[0] = 1;
    dp[1] = 2;
    for (int i = 2; i < n; i++)
    {
      dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n - 1];
  }
};
int main()
{
  Solution solution;
  int step = solution.climbStairs(3);
  std::cout << step << std::endl;
  return 0;
}