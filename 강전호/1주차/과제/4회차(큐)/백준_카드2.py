# N장의 카드 각각 1부터 N까3지 번호  1번카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가놓여있다
# 제일 위에있는 카드버린다
# 제일 위에 있는 카드를 제일 밑으로 옮긴다.
from collections import deque

queue = []

n= int(input())
for i in range(n,0,-1):
    queue.append(i)
queue = deque(queue)

while len(queue)>1:  # 큐에 한장의 카드만 남았을경우
    queue.pop()      # 맨위의 카드 버리기
    last = queue.pop() # 그다음 맨위의카드 지정

    queue.appendleft(last)  # 지정한카드 바닥에 깔기


print(queue.pop())  #마지막 카드 출력

