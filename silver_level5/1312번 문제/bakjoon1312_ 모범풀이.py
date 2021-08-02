a, b, n = map(int, input().split())

r = a%b 

for i in range(n-1):
    r = (r*10)%b
    
print((r*10)//b)