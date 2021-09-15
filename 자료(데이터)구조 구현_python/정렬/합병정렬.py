def merge(a,b,low,mid,high):
    i=low
    j=mid+1
    for k in range(low, high+1): #a의 앞/뒷부분 합병하여 b에 저장
        if i >mid:
            b[k]=a[j]
            j +=1

        elif j >high:
            b[k]=a[i]
            i +=1
        
        elif a[j] < a[i]:
            b[k]=a[j]
            j+=1

        else:
            b[k]=a[i]
            i +=1

    
    for k in range(low, high+1):
        a[k]=b[k]

    
def merge_sort(a,b,low,high):
    if high <=low:
        return
    
    mid=low+(high-low)//2
    merge_sort(a,b,low,mid)
    merge_sort(a,b,mid+1,high)
    merge(a,b,low,mid,high)