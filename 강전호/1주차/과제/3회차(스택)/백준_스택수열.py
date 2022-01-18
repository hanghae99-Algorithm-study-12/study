def stack_su():
    stack =[]
    answer=[]
    temp=[]
    n = int(input())
    for i in range(1,n+1):
        temp.append(i)
    for i in range(0,n):
        a=int(input())
        if not answer and a!=stack[-1]:
            print("NO")
        while temp and a != stack[-1]:
            stack.append(temp.pop())
            answer.append('+')
        if not stack:
            print("NO")
        else:
            stack.pop()
            answer.append('-')
    print(answer)
stack_su()