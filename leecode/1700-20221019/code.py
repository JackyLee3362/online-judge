from collections import Counter
List = list


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_conter = Counter(students)
        for i in sandwiches:
            if stu_conter[i]:
                stu_conter[i] -= 1
                continue
            break
        return stu_conter[0]+stu_conter[1]

    def __call__(self, *args, **kwds):
        myans = self.countStudents(*args)
        self.test(myans, **kwds)

    def test(self, myans, ans):
        if myans != ans:
            print(f"F: {myans} >>> {ans}")
        else:
            print(f"T: {ans}")


Solution()([1, 1, 0, 0], [0, 1, 0, 1], ans=0)
Solution()([1, 1, 0, 0, 1], [0, 1, 0, 1], ans=1)
Solution()([1, 1, 0, 0], [0, 1, 0, 1, 1], ans=0)
Solution()([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], ans=3)
