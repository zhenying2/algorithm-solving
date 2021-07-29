
#solution 1

a=input()
b=input()
K="1234567890"
for i in K:
    a = a.replace(i,"")
if b in a:
    print(1)
else:
    print(0)


#solution 2

s = input()
for i in range(10):
    list = s.split(str(i))
    s = "".join(list)

k = input()

if k in s:
    print(1)
else:
    print(0)