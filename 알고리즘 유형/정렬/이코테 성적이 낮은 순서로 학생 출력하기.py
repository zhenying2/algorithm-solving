import sys
input=sys.stdin.readline

#학생의 수 입력
N=int(input())

students=[]

#학생의 이름, 성적 입력
for _ in range(N):
    name,score=input().split(" ")
    score=int(score) #숫자형으로 형변환
    student=[]
    student.append(name)
    student.append(score)
    students.append(student) #학생의 이름, 성적 이중리스트 형성

#성적 순으로 정렬
students=sorted(students, key=lambda person: person[1])

#원하는 형식으로의 출력
for i in range(N):
    print(students[i][0], end=" ")
