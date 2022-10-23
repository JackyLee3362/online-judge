class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans = [1]
        n = k // 5
        for i in range(2*n):
            for j in range(2*n):
                for t in range(n):
                    ans.append(pow(3, i)*pow(5, j)*pow(7, t))
        ans.sort()
        # print(ans[-100:])
        print("len of ans is ", len(ans))
        print("len of ans is ", len(set(ans)))
        for index, item in enumerate(ans):
            if item == 3215625:
                print(f"No.{index}={item}")
            elif item == 4465125:
                print(f"No.{index}={item}")
                break
        print(ans[:10])


Solution().getKthMdpgicNumber(1)

"""
251
素因子[3,5,7] 
序列：
dp[0] = 1 = [0,0,0]
dp[1] = 3 = [1,0,0]
dp[2] = 5 = [0,1,0]
dp[3] = 7 = [0,0,1]
dp[4] = 9 = [2,0,0]
dp[5] = 15= [1,1,0]
dp[6] = 21= [1,0,1]
dp[7] = 25= [0,2,0]
dp[8] = 27= [3,0,0]

"""
