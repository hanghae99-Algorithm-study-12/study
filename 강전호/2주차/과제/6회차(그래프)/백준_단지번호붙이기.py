# from collections import Counter
#
# n= int(input())
# a=[]
# for i in range(n):
#     a.append(list(map(int, input())))
#
# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
# rows,cols = len(a),len(a[0])
# count=0
# cnt=1
# answer=[]
# for row in range(rows):
#     for col in range(cols):
#
#
#         if a[row][col]!=1:
#             if(count!=0):
#                 answer.append(count)
#             count=0
#             continue
#         count=0
#         cnt+=1
#         stack=[(row,col)]
#
#         while stack:
#
#             x,y=stack.pop()
#
#             if(a[x][y]!=cnt):
#                 count+=1
#             a[x][y]=cnt
#
#             for i in range(4):
#                 nx = x+dx[i]
#                 ny = y+dy[i]
#                 if nx<0 or nx >= rows or ny<0 or ny >= cols or a[nx][ny] != 1:
#                     continue
#                 stack.append((nx,ny))
#
#
#
# print(cnt-1)
# answer = (sorted(answer))
# for i in answer:
#     print(i)


n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
rows, cols = len(grid), len(grid[0])
cnt = 0
count = 0
a = []
for row in range(rows):
    for col in range(cols):
        if grid[row][col] != 1:
            continue

        cnt += 1
        stack = [(row, col)]

        count = 0
        while stack:
            x, y = stack.pop()

            if grid[x][y] != 0: ## 이미 0으로 변경되있던 부분도 0으로 바꾸면서 중복으로 카운트를 세주어서 증가함
                count += 1

            grid[x][y] = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                    continue
                stack.append((nx, ny))
        a.append(count)
print(grid)
print(cnt)
answer = sorted(a)
for i in answer:
    print(i)
