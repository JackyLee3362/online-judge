#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  vector<int> decrypt(vector<int> &code, int k)
  {
    int n = code.size();
    vector<int> ret(n, 0);
    if (k > 0)
      for (int i = 0; i < n; i++)
        for (int j = i + 1; j < i + k + 1; j++)
          ret[i] += code[j % n];
    else if (k < 0)
      for (int i = 0; i < n; i++)
        for (int j = i - 1; j > i + k - 1; j--)
          ret[i] += code[(j + n) % n];
    return ret;
  }
};