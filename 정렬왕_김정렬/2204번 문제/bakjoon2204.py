#백준 정렬왕

while True:

    number=int(input())

    #0을 입력하면 프로그램 반복 종료
    if number == 0:
        break

    #0이 아니라면
    else:
        words=[]

        for i in range(number):
            word=input()

            #입력받은 단어를 words 리스트의 원소로 삽입
            words.append(word)

        #단어를 소문자로 바꾼뒤 -> 정렬
        words.sort(key=lambda word: word.lower())

        #words 리스트 변수의 맨 앞 단어를 출력
        print(words[0])