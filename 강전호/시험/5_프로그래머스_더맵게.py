import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    scoville.sort() # 해도 되고 안해도됨
    answer = 0

    while scoville[0] <= K:
        if len(scoville) == 1: return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer