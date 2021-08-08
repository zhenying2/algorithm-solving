from methods import SimpleList #methods.py에서 SimpleList class를 import

if __name__ == '__main__': #이 파이썬 파일이 메인파일이라면
    s=SimpleList() #단순 연결리스트 생성

    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_after('cherry', s.head.next)
    s.insert_front('pear')
    s.print_list()

    print('cherry는 %d번째' %s.search('cherry'))
    print('kiwi는 ',s.search('kiwi')) #엽결리스트에 없는 원소

    #배 다음노드 삭제후
    s.delete_after(s.head)
    s.print_list()

    #첫번째 노드 삭제후
    s.delete_front()
    s.print_list()

    #망고, 딸기 연결리스트의 맨 앞노드로 차례로 삽입
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()

    #head가 가리키는 노드로부터 이후 3번째 노드 삭제
    s.delete_after(s.head.next.next)
    s.print_list()
