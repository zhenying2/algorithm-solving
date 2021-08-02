import sys

a,b,n=map(int, sys.stdin.readline().split())
int_result=float(a)/float(b)


#문자열의 slice 이용하기 위해 숫자 -> 문자 형변환
str_result=str(int_result)

#소수점 위치 찾기
find=str_result.find('.')
print(int(str_result[find+n]))
