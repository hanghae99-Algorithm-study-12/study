import heapq
from collections import Counter
# def Solution(num,k):
#     answer=[]
#     freqs=Counter(nums)
#     freqs_heap=[]
#
#     for i in freqs:
#         heapq.heappush(freqs_heap,(-freqs[i],i))
#
#     for i in range(k):
#         answer.append(heapq.heappop(freqs_heap)[1])
#     return answer
def Solution(num,k):
    answer=list(zip(*Counter(num).most_common(k)))[0]
    return answer

nums=[5,3,1,1,1,3,73,1]

k = 2
print(Solution(nums,k))
Counter({1: 4, 3: 2, 5: 1, 73: 1})