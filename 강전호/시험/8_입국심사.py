def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (right + left) // 2
        temp = 0
        for i in times:
            temp += mid // i

        if temp >= n:
            answer = mid
            right = mid - 1

        elif temp < n:
            left = mid + 1

    return answer



print(solution(10,[6, 8,10]))
temp=[1,2,3,4]
