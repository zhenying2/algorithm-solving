import sys

raw=sys.stdin.readline()
want_find=sys.stdin.readline().strip()
#fliter 내장함수 이용 => 문자만 원소로 있는 리스트 만들기
#문자인지 확인-> isalpha()내장함수를,
#숫자인지 확인-> isdigit()내장함수를 사용

keyword=list(map(str,filter(str.isalpha,raw)))


#초기 인덱스
index=-1

#첫번째 인덱스 찾기
for i in range(len(keyword)):

    #기존 리스트에 첫번째 원소 찾을 수 있다면 인덱스 값 변화
    if (want_find[0]==keyword[i]):
        index=i
        break

#정확히 모든 문자 있는지 확인
for k in range(len(want_find)):
    #첫번째 문자 확인 불가능할때
    if (index == -1):
        print(0)
        break

    else:
        if (want_find[k]==keyword[index]):
            index=index+1
            #마지막까지 비교가 완료 된 상황
            if (k==len(want_find)-1):
                print(1)

            else:
                continue
        
        else:
            print(0)
            break
