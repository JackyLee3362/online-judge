class Solution
{
public:
  int minOperations(vector<string> &logs)
  {
    int depth = 0;
    for (auto i : logs)
    {
      if (i == "./")
        continue;
      else if (i == "../")
      {
        if (depth > 0)
          depth--;
      }
      else
      {
        depth++;
      }
    }
    return depth;
  }
};