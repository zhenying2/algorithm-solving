#baekjoon 10872
#2022.01.09
#bronze 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
N=int(input())
print(factorial(N))
