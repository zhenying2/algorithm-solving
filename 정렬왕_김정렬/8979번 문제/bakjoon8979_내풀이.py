#정렬왕 김정렬

information=input()
real_information=information.split(' ')
intreal_information=list(map(int,real_information))

#국가의 수
countries=intreal_information[0]

#구하고자 하는 국가의 등수
rank=intreal_information[1]

#나라 정보 입력받는 함수
def inputcountry():
    infor=input()
    realinfor=infor.split(' ')
    intinfor=list(map(int,realinfor))
    return intinfor

#리스트에 나라 정보 저장 (이중 리스트 이용)
c=[]
for i in range(countries):
    c.append(inputcountry())

#금은동 순 내림차순 정렬
c.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True)

#등수를 찾아, index 변수에 저장
for i in range(countries):
    if c[i][0]==rank:
        index=i

#등수가 같은 나라(=공동순위까지 모두 적용) => i+1시켜 출력
for i in range(countries):
    if c[index][1:] == c[i][1:]:
        print(i+1)
        break
