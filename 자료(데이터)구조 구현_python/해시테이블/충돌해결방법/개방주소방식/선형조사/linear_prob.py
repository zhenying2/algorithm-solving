class LinearProbing:
    def __init__(self,size):
        self.M=size #M: 테이블의 크기
        self.a=[None]*size #해시테이블 a
        self.d=[None]*size #데이터 저장용 d

    def hash(self,key):
        return key % self.M #나눗셈 해시함수

    def put(self,key,data): #삽입연산
        initial_position=self.hash(key) #초기위치
        i=initial_position
        j=0
        while True:
            if self.a[i]==None: #빈곳발견
                self.a[i]=key
                self.d[i]=data
                return

            if self.a[i] == key: #이미 key가 해시테이블에 있다면 data만 갱신
                self.d[i]=data
                return
            
            j +=1
            i=(initial_position+j) % self.M

            if i == initial_position: #다음 위치가 초기 위치랑 같다면 루프 벗어나기
                break

    def get(self, key): #탐색 연산
        initial_position=self.hash(key) #초기 위치
        i=initial_position
        j=1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i] #탐색 성공
            
            i=(initial_position+j) %self.M #다음 원소 검색
            j +=1
            if i == initial_position:
                return None #탐색 실패

        return None
