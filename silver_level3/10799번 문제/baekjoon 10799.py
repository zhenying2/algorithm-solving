#baekjoon 10799
#silver level 3
#2022.01.25

import sys

s = sys.stdin.readline().rstrip()
stack = []
result = 0

for i in range(len(s)):
  if s[i] == '(':
    stack.append(i)
  elif s[i] == ')':
    if s[i - 1] == '(':
      stack.pop()
      result += len(stack)
    else:
      result += 1
      stack.pop()

print(result)