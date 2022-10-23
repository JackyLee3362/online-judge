List = list
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      """
      basket:
      第一个表示水果种类，
      第二个表示水果最早出现的位置
      第三个表示水果最晚出现的位置
      """
      n = len(fruits)
      if n == 1:
        return 1
      elif n == 2:
        return 2
      if len(set(fruits)) == 1:
        return n
      
      basket = [[-1,0,-1],[-1,0,-1]]
      def cnt_basket():
        a = [basket[0][1], basket[0][2], basket[1][1], basket[1][2]]
        return max(a) - min(a) + 1
      cnt = 0
      for i, fruit in enumerate(fruits):
        if fruit == basket[0][0]:
          basket[0][2] = i
        elif fruit == basket[1][0]:
          basket[1][2] = i
        else:
          cnt = max(cnt, cnt_basket())
          if basket[0][2] < basket[1][2]:
            basket[1][1] = basket[0][2] + 1 
            # if basket[1][2] >= 0 else basket[1][1]
            basket[0] = [fruit, i, i]
          else:
            basket[0][1] = basket[1][2] + 1 
            # if basket[0][2] >= 0 else basket[0][1]
            basket[1] = [fruit, i, i]
      cnt = max(cnt, cnt_basket())
      return cnt
      
solution = Solution()
# print(solution.totalFruit([1,2,1]),"ans is 3")
# print(solution.totalFruit([0,1,2,2]),"ans is 3")
# print(solution.totalFruit([1,2,3,2,2]),"ans is 4")
# print(solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4]),"ans is 5")
# print(solution.totalFruit([0,1,1]),"ans is 3")
# print(solution.totalFruit([1,0,1,4,1,4,1,2,3]), "ans is 5")
# print(solution.totalFruit([1,0,1,2,2]), "ans is 3")
print(solution.totalFruit([3,3,3,3,3,3]), "ans is 6")


            

