class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        # 找到第一个数
        head = int(k / 2) + 1
        # 判定符号
        if k % 2:
            flag = 1
        else:
            flag = -1
        # answer数组赋初值
        answer = list(range(1, n+1))
        # 构造前k项
        for i in range(k):
            answer[i] = head
            head = flag * (i+1) + head
            flag = -flag
        return answer

solution = Solution()
answer = solution.constructArray(3,2)
print(answer)
        
            

    
        
        
        
        