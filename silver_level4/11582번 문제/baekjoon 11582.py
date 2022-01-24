#baekjoon 11582
#2022.01.24
#silver level 4

import sys

n = int(sys.stdin.readline())
table = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

answer = []

std = n // k
for i in range(k):
    answer.extend(sorted(table[i * std:(i+1) * std]))
print(" ".join(map(str, answer)))