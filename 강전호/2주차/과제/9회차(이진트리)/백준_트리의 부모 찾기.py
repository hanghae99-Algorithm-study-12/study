from collections import defaultdict

N=int(input())
dict=defaultdict(list)
for _ in range(1,N):
    a,b=map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)

answer=[0]*(N-1)

stack=[1]

while stack:
    cur=stack.pop()

    for node in dict[cur]:
        if node == answer[cur-2]:
            continue
        answer[node-2]=cur
        stack.append(node)
for i in answer:
    print(i)
