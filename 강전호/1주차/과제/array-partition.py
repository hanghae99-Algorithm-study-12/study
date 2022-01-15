# n 개의 페어를 이용한 min(a,b)의 합으로 만들수 있는 가장 큰수를 출력해라
# 입력
#       [1,4,3,2]
# 출력
#       4

def arrayPairSum(nums):
    nums.sort()
    answer = 0
    for i in range(len(nums)):
        if (i % 2 == 0):
            answer += nums[i]
    return answer


nums = [1, 4, 3, 2]
print(arrayPairSum(nums))
