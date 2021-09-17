def qsort(a,low,high):
    if low < high:
        pivot=partition(a,low,high) #피벗을 기준으로 분할
        qsort(a,low,pivot-1) #앞부분 재귀호출
        qsort(a,pivot+1,high) #뒷부분 재귀호출

def partition(a,pivot,high):
    i=pivot+1
    j=high

    while True:
        while i<high and a[i]<a[pivot]:
            i +=1

        while j>pivot and a[j]>a[pivot]:
            j-=1

        if j <=i:
            break

        a[i],a[j]=a[j],a[i]

        i +=1
        j -=1

    a[pivot],a[j]=a[j],a[pivot]
    return j