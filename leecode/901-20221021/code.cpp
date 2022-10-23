#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;
class StockSpanner
{
public:
    stack<pair<int, int>> monoStack;
    StockSpanner()
    {
    }

    int next(int price)
    {
        pair<int, int> next(price, 1);
        while (!monoStack.empty() && price >= monoStack.top().first)
        {
            pair<int, int> tmp = monoStack.top();
            next.second += tmp.second;
            monoStack.pop();
        }
        monoStack.push(next);
        return next.second;
    }
};
int main()
{
    int nums[7] = {100, 80, 60, 70, 60, 75, 85};
    StockSpanner stock;
    for (auto i : nums)
    {
        cout << stock.next(i) << endl;
    }
    return 0;
}