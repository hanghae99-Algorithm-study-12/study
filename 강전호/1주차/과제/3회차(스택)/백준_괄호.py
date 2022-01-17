# num = int(input())
#
# for i in range(num):
#     stack = []
#     s = input()
#     check = True
#     for char in s:
#
#         if char == "(":
#             stack.append(char)
#         else:
#             if not stack:
#                 print("NO")
#                 check = False
#                 break
#             stack.pop()
#
#
#     if check ==True: # 체크 변수를 넣어준 이유 : 위에 포문에서 닫이는 괄호가 나왔는데 스택이 비어있는경우 노를 프린트하고 밑으로 내려와서 스택이 비어있으면 예스를 한번 더 출력하기 때문
#         if not stack :
#             print("YES")
#         else:
#             print("NO")


### 그러나 check 변수를 사용하고 싶지 않아서 찾아보니 for-else 문으로 for문에서 한번도 break가 난적이 없다면 else문을 실행
# num = int(input())
# for i in range(num):
#     stack = []
#     s = input()
#     for char in s:
#
#         if char == "(":
#             stack.append(char)
#         else:
#             if not stack:
#                 print("NO")
#                 break
#             stack.pop()
#     else:
#         if not stack :
#             print("YES")
#         else:
#             print("NO")


### 스택 구현해서 풀기
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None
        topNode = self.top
        self.top = self.top.next
        return topNode.item

    def is_empty(self):
        return self.top is None


num = int(input())
for i in range(num):
    stack = Stack()
    s = input()
    for char in s:

        if char == "(":             #여는 괄호인 경우
            stack.push(char)        #stack에 푸시
        else:                       #닫는 괄호인 경우
            if stack.is_empty():           #스택이 비어있다면
                print("NO")
                break
            stack.pop()

    else:                       # for - else 문을 써주는 이유 : 닫는 괄호가 남아있지만 스택에 여는 괄호가 없이 비어있는 상태로 No가 출력 되고 break에 걸리고
                                # else를 안써주게 되면 비어있는 스택때문에 YES를 한번 더 출력하게 됨 ( for-else 문은 for문에서 break가 안걸리면 else를 감)
                                # break 에 걸려서 뒤에 else문을 안감
        if stack.is_empty() :          # 스택이 비어있으면 YES
            print("YES")
        else:                   # 스택이 안 비어있으면 No 브레이크에 안걸렸더라도 즉 여는 괄호는 남아있는상태로 오면
            print("NO")
