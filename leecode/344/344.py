s = ["h","e","l","l","o"]
length = len(s)
for i in range(length >> 1):
  s[i],s[length-1-i] = s[length-1-i], s[i]
print(s)

  