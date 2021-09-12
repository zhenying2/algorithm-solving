def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i,0,-1): #현재 원소가 정렬된 부분에 삽입될 곳을 찾음
            if a[j-1] >a[j]:
                a[j],a[j-1]=a[j-1],a[j] #현재 원소와 바로 앞의 원소 교환


