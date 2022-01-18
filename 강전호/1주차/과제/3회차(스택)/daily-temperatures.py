# 매일의 화씨 온도 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야하는지를 출력하라
# T = [73, 74, 75, 71, 69, 72, 76, 73]
#    [1, 1, 4, 2, 1, 1, 0, 0]

#
# 시간초과
# for i in range(0,len(T)):
#     for j in range(i,len(T)):
#         if T[i]<T[j]:
#             print(j-i)
#             break
#         else:
#             if j == len(T)-1:
#                 print(0)

T = [73, 74, 75, 71, 69, 72, 76, 73]
def dailyTemperatures(T):
    stack=[]
    answer = [0]* len(T)
    for i ,j in enumerate(T):
        while stack and j>T[stack[-1]]:
            last = stack.pop()
            answer[last] =i-last
        stack.append(i)

    return answer
print(dailyTemperatures(T))