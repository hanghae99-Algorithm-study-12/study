from collections import defaultdict

N=int(input())
dict=defaultdict(list)
for _ in range(1,N):
    a,b=map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)
print(dict)

answer=[0]*(N-1)

for i in range(1,N):
    dict[i]
