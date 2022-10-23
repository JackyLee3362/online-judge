class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        n, m = len(arr), len(pieces)
        index = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < n:
            if arr[i] not in index:
                return False
            p = pieces[index[arr[i]]]
            if p != arr[i:i+len(p)]:
                return False
            i += len(p)
        return True
