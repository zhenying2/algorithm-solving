import sys

raw=sys.stdin.readline()
want_find=sys.stdin.readline().strip()

keyword=list(map(str,filter(str.isalpha,raw)))
keywords="".join(keyword)

if keywords.find(want_find) != -1:
    print(1)
else:
    print(0)