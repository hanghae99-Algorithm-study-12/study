# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
# 입력
#       nums=[-1,0,1,2,-1,4]
# 출력
#       [
#           [-1,0,1],
#           [-1,-1,2]
# from itertools import combinations
# def threeSum(nums):
#     answer = []
#     for i in list(combinations(nums, 3)):
#         if (sum(i) == 0):
#
#             answer.append(list(i))
#
#     temp = []
#     for i in answer:
#         if sorted(i) not in temp:
#             temp.append(sorted(i))
#
#
#     return temp
# 시간초과
from itertools import combinations


def threeSum(nums):
    answer = []
    nums.sort()
    
    return answer


nums = [-1, 0, 1, 2, -1, 4]

print(threeSum(nums))
