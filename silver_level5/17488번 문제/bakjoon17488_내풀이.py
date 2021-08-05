import sys

#공백을 기준으로 두개의 변수에 동시 할당
people, subject = map(int, sys.stdin.readline().split())

#과목 제한 인원 입력받기
limit=list(map(int, sys.stdin.readline().split()))
#수강바구니 과목-제한인원 쌍의 dict 만들기
baggage={}
for i in range(subject):
    baggage[i+1]=limit[i]

total_baggage=[]

#1차 수강바구니
for i in range(people):
    sample=list(map(int, sys.stdin.readline().split()))
    sample.remove(-1)
    total_baggage.append(sample)

total1=[]
#과목별 1차 수강신청 인원 수 합 정리
for i in range(subject):
    counts=0
    for j in range(people):
        counts+=total_baggage[j].count(i+1)
    total1.append(counts)

#1차 성공과목 확인
for i in range(subject):
    #과목제한인원 < 수강신청인원
    if (baggage[i+1] < total1[i]):
        for j in range(people):
            if (i+1 in total_baggage[j]):
                total_baggage[j].remove(i+1)
        baggage[i+1]=0
    
    #과목제한인원 >= 수강신청인원
    else:
        for j in range(people):
            if (i+1 in total_baggage[j]):
                limit[i]-=1
        baggage[i+1]=limit[i]  

total_baggage2=[]

#2차 수강바구니
for i in range(people):
    sample=list(map(int, sys.stdin.readline().split()))
    sample.remove(-1)
    total_baggage2.append(sample)

total2=[]
#과목별 2차 수강신청 인원 수 합 정리
for i in range(subject):
    counts=0
    for j in range(people):
        counts+=total_baggage2[j].count(i+1)
    total2.append(counts)

#2차 성공과목 확인
for i in range(subject):
    #과목제한인원 < 수강신청인원
    if (baggage[i+1] < total2[i]):
        for j in range(people):
            if (i+1 in total_baggage2[j]):
                total_baggage2[j].remove(i+1)
        baggage[i+1]=0
    
    #과목제한인원 >= 수강신청인원
    else:
        for j in range(people):
            if (i+1 in total_baggage2[j]):
                limit[i]-=1
        baggage[i+1]=limit[i]

#1차 2차 성공과목 합치기 => extend 함수 사용
for i in range(people):
    total_baggage[i].extend(total_baggage2[i])
    
#결과 출력 (채점 기준 원하는대로)
for i in range(people):
    if (total_baggage[i] == []):
        print("망했어요")
    else:
        for j in range(len(total_baggage[i])):
            print(total_baggage[i][j], end=" ")
        print()
