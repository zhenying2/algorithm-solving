def selection_sort(a):
    for i in range(0,len(a)-1):
        min=i
        for j in range(i,len(a)):
            if a[min] > a[j]:
                min=j #정렬 안된곳에서 최솟값 찾기

        a[i],a[min]=a[min],a[i] #현재의 원소와 최솟값 가진 원소와 교환