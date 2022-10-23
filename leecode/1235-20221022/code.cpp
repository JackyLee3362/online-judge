#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// class Solution
// {
// public:
//     struct Job
//     {
//         int start;
//         int end;
//         int profit;
//     };
//     int jobScheduling(vector<int> &startTime, vector<int> &endTime, vector<int> &profit)
//     {
//         vector<Job> jobs;
//         int n = startTime.size();
//         for (int i = 0; i < n; i++)
//             jobs.push_back(Job{startTime[i], endTime[i], profit[i]});
//         sort(jobs.begin(), jobs.end(), [](Job a, Job b) -> bool
//              { return a.end <= b.end; });
//         vector<int> dp(n + 1);
//         for (int i = 0; i <= n; i++)
//         {
//             int k = upper_bound(jobs.begin(), jobs.begin() + i - 1, jobs[i - 1].start, [&](int st, const vector<int> &job) -> bool
//                                 { return st < job[1]; }) -
//                     jobs.begin();
//             dp[i] = max(dp[i - 1], dp[k] + jobs[i - 1].end);
//         }
//         return dp[n];
//     }
// };
class Solution
{
public:
    int jobScheduling(vector<int> &startTime, vector<int> &endTime, vector<int> &profit)
    {
        int n = startTime.size();
        vector<vector<int>> jobs(n);
        for (int i = 0; i < n; i++)
        {
            jobs[i] = {startTime[i], endTime[i], profit[i]};
        }
        sort(jobs.begin(), jobs.end(), [](const vector<int> &job1, const vector<int> &job2) -> bool
             { return job1[1] < job2[1]; });
        vector<int> dp(n + 1);
        for (int i = 1; i <= n; i++)
        {
            int k = upper_bound(jobs.begin(), jobs.begin() + i - 1, jobs[i - 1][0], [&](int st, const vector<int> &job) -> bool
                                { return st < job[1]; }) -
                    jobs.begin();
            dp[i] = max(dp[i - 1], dp[k] + jobs[i - 1][2]);
        }
        return dp[n];
    }
};

int main()
{
    Solution solution;
    vector<int> startTime = {1, 2, 3, 3};
    vector<int> endTime = {3, 4, 5, 6};
    vector<int> profit = {50, 10, 40, 70};
    solution.jobScheduling(startTime, endTime, profit);
    return 0;
}