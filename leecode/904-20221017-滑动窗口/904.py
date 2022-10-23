List = list
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      """
      basket:
      第一个表示水果种类，
      第二个表示水果数量，
      第三个表示水果最后一次出现的位置
      """
      basket = [[-1,0,-1],[-1,0,-1]] # 
      cnt = 0
      for n,fruit in enumerate(fruits):
        if fruit == basket[0][0]:
          basket[0][1] += 1
          basket[0][2] = n
        elif fruit == basket[1][0]:
          basket[1][1] += 1
          basket[1][2] = n
        else:
          cnt = max(cnt, basket[0][1]+basket[1][1])
          if basket[0][2] <= basket[1][2]:
            basket[0] = [fruit, 1, n]
          else:
            basket[1] = [fruit, 1, n]
      return max(cnt, basket[0][1]+basket[1][1])
solution = Solution()
# print(solution.totalFruit([1,2,1]),"ans is 3")
# print(solution.totalFruit([0,1,2,2]),"ans is 3")
# print(solution.totalFruit([1,2,3,2,2]),"ans is 4")
# print(solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4]),"ans is 5")
# print(solution.totalFruit([0,1,1]),"ans is 3")
# print(solution.totalFruit([1,0,1,4,1,4,1,2,3]), "ans is 5")
print(solution.totalFruit([1,0,1,2,2]), "ans is 3")


            

