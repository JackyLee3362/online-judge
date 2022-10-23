List = list
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        max_target = target[-1]
        for i in range(1,n+1):
            ans.append("Push")
            if i == max_target:
                break
            if not i in target:
                ans.append("Pop")
        return ans
            
solution = Solution()
print(solution.buildArray([1,3],3))
print(solution.buildArray([1,2,3],3))
print(solution.buildArray([1,2],4))