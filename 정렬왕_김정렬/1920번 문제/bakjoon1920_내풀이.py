#백준_정렬왕
#문제: 1920번 내 풀이

size=int(input())
numbers=input()
arrayA= numbers.split(' ')

#arrayA의 리스트 원소들 문자 -> 숫자로 형변환
intarrayA=list(map(int,arrayA))
intarrayA.sort()
print(intarrayA)
#비교할 정수의 크기
comparesize=int(input())

numbers2=input()
arrayB=numbers2.split(' ')

#arrayB의 리스트 원소들 문자-> 숫자로 형변환
intarrayB=list(map(int,arrayB))

for i in intarrayB:
    for k in range(size):
        if i == intarrayA[k]:
            print(1)
            break
        else:
            k=k+1
            if k == size:
                print(0)



        
