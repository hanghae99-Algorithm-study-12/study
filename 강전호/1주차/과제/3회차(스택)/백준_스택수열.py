def stack_su():
    stack =[]
    answer  =[]
    n = int(input())  # 8 (입력 개수)
    arr = [int(input()) for _ in range(n)]  # [4, 3, 6, 8, 7, 5, 2, 1] (입력 배열)
    index = 0

    for i in range(1,n+1):          # 1 2 3 4 5 6 7 8
        stack.append(i)             # 스택이 비어있으면 안되서
        answer.append('+')

        while stack and stack[-1] == arr[index]:     # 스택이 안비어있고 스택의 마지막이 배열의 인덱스와 같으면
            stack.pop()
            answer.append('-')
            index+=1                                    #인덱스 올려주기
    if stack:
        print("No")
    else:
        for i in answer:
            print(i)


stack_su()