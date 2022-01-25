import math

def solution(progresses, speeds):
    maintain = []
    for i in range(0, len(progresses)):
        maintain.append(math.ceil((100 - progresses[i]) / speeds[i]))

    answer = []
    temp = maintain[0]
    cnt = 0
    for i in maintain:
        if temp >= i:
            cnt += 1

        else:
            answer.append(cnt)
            cnt = 1
            temp = i
    answer.append(cnt)

    return answer


solution([93, 30, 55], [1, 30, 5])
