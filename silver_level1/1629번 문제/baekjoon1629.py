# 22.07.10
# time over

def SmartMultiply(a,b,c):
    result=1

    # 종료조건
    if b==1:
        return a%c

    sample_result=SmartMultiply(a,b//2,c)
    
    # b번이 짝수라면
    if (b%2==0):
        return sample_result*sample_result %c

    # b번이 홀수라면
    elif (b%2!=0):
        return a*sample_result*sample_result %c

a,b,c=map(int,input().split())

print(SmartMultiply(a,b,c))
