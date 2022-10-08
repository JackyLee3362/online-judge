#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  vector<int> constructArray(int n, int k)
  {
    int head = k / 2 + 1;
    int flag;
    if (k % 2)
      flag = 1;
    else
      flag = -1;
    vector<int> answer(n, 0);
    for (int i = 0; i < n; i++)
    {
      if (i < k)
      {
        answer[i] = head;
        head += flag * (i + 1);
        flag *= -1;
      }
      else
      {
        answer[i] = i + 1;
      }
    }
    return answer;
  }
};

int main()
{
  Solution solution;
  vector<int> answer;
  answer = solution.constructArray(3, 2);
  for (auto i : answer)
  {
    cout << i << endl;
  }
  return 0;
}