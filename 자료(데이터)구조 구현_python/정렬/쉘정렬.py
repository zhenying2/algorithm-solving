def shell_sort(a):
    h=4
    while h >=1:
        for i in range(h, len(a)): #h-정렬 수행
            j=i
            while j >=h and a[j] < a[j-h]:
                a[j], a[j-h]=a[j-h],a[j]
                j -=h
        
        h //=3 #다음 h값 계산