#baekjoon 1085
#bronze level3
#2022.01.14

x,y,w,h=map(int,input().split())

x0=x
y0=y
x1=w-x
y1=h-y

print(min(x0,y0,x1,y1))
