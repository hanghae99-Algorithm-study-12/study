import itertools

def solution(numbers, target):
    answer = 0
    temp = [0]
    for i in range(len(numbers)):
        a = []
        a = (list((itertools.combinations(numbers, i + 1))))

        b = (list(map(sum, a)))
        for i in b:
            temp.append(i * 2)

    for i in temp:
        if sum(numbers) - i == target:
            answer += 1

    return answer

n=[1,1,1,1,1]
t=3
print(solution(n,t))