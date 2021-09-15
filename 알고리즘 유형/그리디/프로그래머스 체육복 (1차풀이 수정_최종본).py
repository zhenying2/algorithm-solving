def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    #여벌 체육복 가져온 사람이 도난 당한 경우 미리 생각 중복리스트 확인
    real_lost= list(set(lost) - set(reserve))
    real_reserve= list(set(reserve) - set(lost))
    
    init=n-len(real_lost) # 초기 빌려주기전, 체육수업 들을 수 있는 학생수
    answer=init

    real_reserve.sort()
    real_lost.sort()
    
    if len(real_lost) != 0 :
        #lost와 reserve 비교 후, 들을 수 있는 학생 수 계산
        for i in real_lost:
            for j in real_reserve:
                if j-1 == i or j+1 == i:
                    answer +=1
                    real_reserve.remove(j)
                    break
    
    return answer
