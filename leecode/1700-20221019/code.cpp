#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution
{
public:
  int countStudents(vector<int> &students, vector<int> &sandwiches)
  {
    int s1 = accumulate(students.begin(), students.end(), 0);
    int s0 = students.size() - s1;
    int sand_len = sandwiches.size();
    for (int i = 0; i < sand_len; i++)
    {
      if (sandwiches[i] == 1 && s1 > 0)
        s1--;
      else if (sandwiches[i] == 0 && s0 > 0)
        s0--;
      else
        break;
    }
    return s0 + s1;
  }
};
int main()
{
  Solution solution;
  vector<int> students = {1, 0, 1, 0};
  vector<int> sandwitches = {1, 1, 0, 1};
  cout << solution.countStudents(students, sandwitches) << endl;
  return 0;
}