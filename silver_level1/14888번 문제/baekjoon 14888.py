#baekjoon 14888
#2022.01.28
#silver level 1

from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

op = []
op += ['+'] * add
op += ['-'] * sub
op += ['*'] * mul
op += ['%'] * div

operators = []
for i in list(permutations(op)):
    operators.append(i)
res_list = []
for i in operators:
    res = num_list[0]
    for j in range(n-1):
        if i[j] == '+':
            res += num_list[j+1]
        elif i[j] == '-':
            res -= num_list[j+1]
        elif i[j] == '*':
            res *= num_list[j+1]
        else:
            if res < 0:
                res = -(-res // num_list[j+1])
            else:
                res //= num_list[j+1]
    res_list.append(res)
        
print(max(res_list))
print(min(res_list))