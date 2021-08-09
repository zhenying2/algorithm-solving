from methods import DoubleList

if __name__ == '__main__':
    s=DoubleList()

    s.insert_after(s.head, 'apple')
    s.insert_before(s.tail,'orange')
    s.insert_before(s.tail,'cherry')
    s.insert_after(s.head.next,'pear')
    s.print_list()

    
    #마지막 노드 삭제후
    s.delete(s.tail.prev)
    s.print_list()

    #맨 끝에 포도 삽입
    s.insert_before(s.tail,'grape')
    s.print_list()

    #첫 노드 삭제
    s.delete(s.head.next)
    s.print_list()

    #첫 노드 삭제
    s.delete(s.head.next)
    s.print_list()

    #첫 노드 삭제
    s.delete(s.head.next)
    s.print_list()

    #첫 노드 삭제
    s.delete(s.head.next)
    s.print_list()

