from typing import Any


class Solution:
    def __init__(self) -> None:
        self.val = 0
        self.ans = 123

    def hello(self, name, num):
        return num
class Test:
    def __init__(self, cls, func) -> None:
        pass
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        myans = self.hello(*args)
        self.test(myans, **kwds)

    def test(self, myans, ans):
        if myans != ans:
            print(f"False: my ans is {myans} !=  ans is {ans}")
        else:
            print(f"True: ans = {ans}")


Solution()("lijie", 1, ans=1)
