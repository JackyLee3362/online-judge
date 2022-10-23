class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        len_arr = len(arr)
        for sub in pieces:
            n = len(sub)
            if not sub[0] in arr:
                return False
            first = arr.index(sub[0])
            for i in range(1, n):
                if i+first >= len_arr or not sub[i] == arr[i+first]:
                    return False
        return True


solution = Solution()
print(solution.canFormArray([15, 88], [[88], [15]]))
print(solution.canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]))
print(solution.canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]
                            ))
