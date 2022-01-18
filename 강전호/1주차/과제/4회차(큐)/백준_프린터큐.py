import sys
from collections import deque

a= int(input())

for i in range(a):
    num,cur = map(int, input().split())
    important=[]
    important =list(map(int, sys.stdin.readline().split())) # 중요도
    queue=deque(important)
    count=0
    while queue:
        best = max(queue)               #가장 중요한일
        front =queue.popleft()          #가장 처음있는 일을 뺴본다.
        cur-=1                          #하나 뺴니까 인덱스를 왼쪽으로 이동
        if(best==front): #가장 중요한게 맨처음
            count +=1                   #일을 처리한 횟수1더해주기
            if cur<0:                   # 가장 중요한 일을 뻈는데 궁금한 인덱스가 음수면 내가 궁금했던일이 가장 중요도가 큰일
                print(count)
                break
        else:                           #중요하지 않은일을뺀경우
            queue.append(front)         # 뒤로 다시 삽입
            if cur<0:                   # 뒤로 다시 삽입하는게 궁금한 일인 경우 아닌경우 위에서 -1 을 해줬음
                cur= len(queue)-1       # 인덱스를 가장 마지막으로 다시 지정




