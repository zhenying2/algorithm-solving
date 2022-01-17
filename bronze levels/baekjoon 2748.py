#baekjoon 2748
#2022.01.17
#time over -> 재귀함수 호출해서인듯

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
N=int(input())
print(fibonacci(N))
