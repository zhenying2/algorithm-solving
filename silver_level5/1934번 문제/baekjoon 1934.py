#baekjoon 1934
#2022.01.20

#최소공배수 구하는 함수
def LCM(a,b):
    minimum=min(a,b)
    lcm=1

    #1과 다른수라면, 최대값 = 최소공배수
    if minimum==1:
        return max(a,b)
    else:
        lists=[]
        i=2
        while (i <= minimum):
            if (a % i == 0 and b %i==0):
                lists.append(i)
                a=int(a//i)
                b=int(b//i)
            else:
                i+=1

        #서로소, 안나눠진값 or 1 리스트에 추가        
        lists.append(a)
        lists.append(b)

        for j in lists:
            lcm*=j
        return lcm
    
case=int(input())

for _ in range(case):
    A,B=map(int,input().split())
    print(LCM(A,B))
    
