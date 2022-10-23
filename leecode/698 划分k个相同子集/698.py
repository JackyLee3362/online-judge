from collections import Counter

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 剪枝
        nums.sort(reverse=True)
        n = len(nums)
        total = sum(nums)
        per = total // k
        if total % k or nums[0] > per:
            return False
        # 遍历记录
        v = [0 for i in range(n)]
        loc = 0
        # 深度递归

        def dfs(idx, cur, cnt, vis):
            '''
            idx(int)       : 搜索下标
            cur(int)       : 当前值
            cnt(int)       : 当前已经满的桶数
            vis(int[n])    : 已经使用过的数
            '''
            if cnt == k:
                return True
            elif cur == per:
                return dfs(loc+1, 0, cnt+1, vis)
            for i in range(idx, n):
                if vis[i] or cur + nums[i] > per:  # 可行性剪枝
                    continue
                vis[i] = 1
                if dfs(i+1, cur + nums[i], cnt, vis):
                    return True
                vis[i] = 0   # 回溯
                if cur == 0:  # 可行性剪枝
                    return False
            return False
        return dfs(loc, 0, 0, v)  
        

solution = Solution()
print(solution.canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4))