def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n  #7분걸리는 심사대랑 10분 걸리는 심사대가 6명
    while left <= right:
        mid = (right + left) // 2
        temp = 0

        for i in times: # 30분이 시간이 있으면 7분걸리는심사대는 4명을볼수있고 10분걸리는심사대는 3명을볼수있다.-> 7명을 검사할수있다.
            temp += mid // i

        if temp >= n:
            answer = mid
            right = mid - 1

        elif temp < n:
            left = mid + 1

    return answer

print(solution(6,[7, 10]))