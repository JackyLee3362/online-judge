class Solution:
    def minOperations(self, logs: list[str]) -> int:
      depth = 0
      for i in logs:
        if i == "../":
          if depth > 0:
            depth -= 1
        elif i == "./":
          continue
        else:
          depth += 1

      return depth