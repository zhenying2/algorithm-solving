#baekjoon 10870
#bronze level 2
#2022.01.11

def Fibonacci(x):
    if x == 0 :
        return 0
    elif x==1:
        return 1
    elif x >=2:
        result=Fibonacci(x-1)+Fibonacci(x-2)
        return result

N=int(input())
print(Fibonacci(N))
