List = list

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
      d_length = len(digits)
      for i in range(d_length):
        digits[i] = ord(digits[i]) - ord('0')
      hash_ = [[0,0] for _ in range(10)]
      
      for i in range(1,10):
        if i in digits:
          hash_[i] = [1,hash_[i-1][1] + 1] if i in digits else [0,hash_]
        else:
          hash_[i][1] = hash_[i-1][1]

      n_list = []
      while n > 0:
        n_list.append(n % 10)
        n //= 10
      n_list.reverse()
      n_length = len(n_list)

      ans = 0
      for i in range(1,n_length):
        ans += pow(d_length, i)
      for i, num in enumerate(n_list):
        if num == 0:
          break
        if i == n_length - 1:
          ans += hash_[num][1]*pow(d_length, n_length - i - 1)
          break
        ans += hash_[num-1][1]*pow(d_length, n_length - i - 1)
        if not hash_[num][0]:
          break
      return ans
      
solution = Solution()
print(solution.atMostNGivenDigitSet(digits = ["1", "4", "9"], n = 415),"ans is 23")
print(solution.atMostNGivenDigitSet(digits = ["1","3","5","7"], n = 100),"ans is 20")
print(solution.atMostNGivenDigitSet(digits = ["1","4","9"], n = 1000000000),  "ans is 29523")
print(solution.atMostNGivenDigitSet(digits = ["7"], n = 8), "ans is 1")
print(solution.atMostNGivenDigitSet(digits = ["1","2","9"], n = 128), "ans is 17")
print(solution.atMostNGivenDigitSet(digits = ["1","4","8"], n = 557), "ans is 30")
print(solution.atMostNGivenDigitSet(digits = ["3","4","8"], n = 4), "ans is 2")
print(solution.atMostNGivenDigitSet(["3","4","5","6"],64), "ans is 18")
print(solution.atMostNGivenDigitSet(["1","5","7","8"],10212),"ans is 340")