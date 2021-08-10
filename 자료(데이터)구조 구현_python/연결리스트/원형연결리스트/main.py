from methods import CircleList

if __name__ == '__main__':
    s=CircleList()

    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.print_list()

    #s의 길이
    print(s.no_items())

    #s의 첫항목
    print(s.first())

    #s의 첫노드 삭제후
    s.delete()
    s.no_items()
    s.print_list()

    #s의 첫노드 삭제후
    s.delete()
    s.no_items()
    s.print_list()

    #s의 첫노드 삭제후
    s.delete()
    s.no_items()
    s.print_list()

    #s의 첫노드 삭제후
    s.delete()
    s.no_items()
    s.print_list()
    