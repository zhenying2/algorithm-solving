def binary_search(array, target, start, end):
	if start > end:
		return None

	mid= (start+end)//2
	
	if array[mid] == target:
		return mid

	#찾고자 하는 값이 중간점의 작보다 작은 경우 중간점의 왼쪽을 재탐색
	elif array[mid] > target:
		return binary_search(array, target, start, mid-1)

	#중간점의 값보다 찾고자 하는 값이 큰 경우 중간점의 오른쪽을 재탐색
	else:
		return binary_search(array, target, mid+1, end)

#가게의 부품 개수 입력
N=int(input())
listA=list(map(int,input().split()))
listA.sort()

#손님이 원하는 부품 입력
M=int(input())
listB=list(map(int,input().split()))

for i in listB:
    result=binary_search(listA,i,0,N-1)

    if result != None:
        print('yes', end=" ")

    else:
        print('no',end=" ")
