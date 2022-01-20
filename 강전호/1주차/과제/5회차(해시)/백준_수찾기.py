import sys
#
# n = int(input())
# a=[]
# b=[]
# a=set(map(int, sys.stdin.readline().split()))
# m = int(input())
# b =list(map(int, sys.stdin.readline().split()))
# print(a)
# for i in b:
#     if i in a :
#         print(1)
#     else:
#         print(0)
N = map(int, sys.stdin.readline())
keyList = list(map(int, sys.stdin.readline().split()))
pool = {}
for k in keyList:
    pool[k] = 1
print(pool)
M = map(int, sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
for t in target:
    if t in pool:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")

#그냥 리스트로 받아서 선형 탐색으로 풀면 시간초과가 뜬다. list형의 containment 연산의 시간 복잡도는 O(n)이기 때문에 containment연산의 시간 복잡도가 O(1)인 set자료형을 사용해