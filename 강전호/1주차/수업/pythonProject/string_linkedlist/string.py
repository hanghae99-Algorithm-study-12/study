if __name__ == "__main__":
    s = "hello"
    print(s[1])  # indexing
    print(s[-1])  # indexing reverse order
    print(s[1:])  # slicing (***) substring
    print(s[1:len(s)])
    print(len(s))  # 길이구하기
    # slicing
    # [start:end] (end 미포함)
    # start : 0 , end : len(s)

    # in 연산자 ( 문자열 안에 문자열 포함되는지?)
    # return 값은 boolean
    print("s" in "str")

    idx = s.index('e')  # return index
    print(idx)
    # list, str
    # join: list -> str
    li = ['1', '2', '3', '4']
    s1 = "".join(li)
    # '1' + '2' + '3' + '4'
    print(s1)
    #immutable (수정불가) list는 수정가능 str은 수정불가능
    #s1[0] = '10' -> str이 수정하려고 해서 에러남남
    s = 'hhhh'
    cnt = s.count('h')
    print(cnt)