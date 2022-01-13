#baekjoon 2869
#2022.01.13 구글+다른사람 풀이
#bronze level 1
#연산항 변환 -> 반복문 없이 일수를 표현 -> timeoverX

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
