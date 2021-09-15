#1차 풀이, 중복이 되는 도난당한 사람 경우가 오류남...

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    #여벌 체육복 가져온 사람이 도난 당한 경우 미리 생각
    for i in reserve:
        for j in lost:
            if i == j:
                lost.remove(j)
                reserve.remove(i)

    init=n-len(lost) # 초기 빌려주기전, 체육수업 들을 수 있는 학생수
    answer=init

    lost.sort()
    reserve.sort()
    
    if len(lost) != 0 :
        #lost와 reserve 비교 후, 들을 수 있는 학생 수 계산
        for i in lost:
            for j in reserve:

                if j-1 == i or j+1 == i:
                    answer +=1
                    reserve.remove(j)
                    break
    
    
    return answer
