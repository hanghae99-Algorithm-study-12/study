def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0 :
                triangle[i][j]+= triangle[i-1][j]

            elif j==i:
                triangle[i][j] += triangle[i - 1][j-1]

            else:
                triangle[i][j] += triangle[i - 1][j - 1] if triangle[i - 1][j - 1] > triangle[i - 1][j] else triangle[i-1][j]
    answer=max(triangle[len(triangle)-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
for i in range(5):
    print(i)
print(len([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))