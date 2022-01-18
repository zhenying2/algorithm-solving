#baekjoon 4153
#2022.01.18
#bronze level 4

burgers=[]
drinks=[]

#버거 가격 입력
for _ in range(3):
    burger=int(input())
    burgers.append(burger)

#음료 가격 입력
for _ in range(2):
    drink=int(input())
    drinks.append(drink)

#버거, 음료 크기순으로 정렬
burgers.sort()
drinks.sort()

#가장 싼 세트메뉴 가격 출력
price=burgers[0]+drinks[0]-50
print(price)
