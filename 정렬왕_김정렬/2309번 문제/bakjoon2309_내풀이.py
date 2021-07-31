import sys

#난쟁이 키 저장 리스트
raw_tall=[]

for _ in range(9):
    raw_tall.append(int(sys.stdin.readline()))

tall=sum(raw_tall)


for i in range(len(raw_tall)-1):
    
    for j in range(i+1,len(raw_tall)):

        #9명 -> 7명의 난쟁이만 생각, 즉 2명의 난쟁이 키 뺐을 때 100이라면
        if tall-(raw_tall[i]+raw_tall[j])==100:
            #del을 통한 인덱스번호 제거시 -> 하나 제거시 그 뒤 모든 인덱스 값변화로,
            #index value error 계속 발생함... 따라서
            #remove를 통한 원소 제거로 풀어야함
            a=raw_tall[i]
            b=raw_tall[j]

            raw_tall.remove(a)
            raw_tall.remove(b)
            break

raw_tall.sort()
for l in range(len(raw_tall)):
    print(raw_tall[l])

        