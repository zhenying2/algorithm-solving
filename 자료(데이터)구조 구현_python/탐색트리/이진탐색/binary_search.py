a=[] #탐색하고자 하는 수배열이 있는 리스트

def binary_search(left,right,t):
    if left > right:
        return None #탐색 실패, t가 리스트에 없음

    mid=(left+right)//2

    if a[mid] == t : return mid #탐색 성공
    if a[mid] > t: binary_search(left,mid-1,t) #앞부분 탐색
    else: binary_search(mid+1,right,t) #뒷부분 탐색