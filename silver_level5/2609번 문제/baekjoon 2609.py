#baekjoon 1085
#silver level5
#2022.01.14

x,y=map(int,input().split())

#최대공약수
GreatestCommonFactor=[]

#최소공배수
LeastCommonMultiple=[]

i=2
while (i <= min(x,y)):
    if ( x%i == 0 and y%i==0):
        GreatestCommonFactor.append(i)
        LeastCommonMultiple.append(i)
        x=int(x//i)
        y=int(y//i)
    else:
        i+=1


#나눠 안떨어진 값 or 서로소들-> 최소공배수 리스트에 추가
LeastCommonMultiple.append(x)
LeastCommonMultiple.append(y)

#서로소일 경우 1을 리스트에 넣기
if (not GreatestCommonFactor): #빈 리스트의 경우
    GreatestCommonFactor.append(1)

GCF=1
LCM=1
#최대공약수 출력
for a in GreatestCommonFactor:
    GCF*=a

#최소공배수 출력
for b in LeastCommonMultiple:
    LCM*=b

print(GCF)
print(LCM)
