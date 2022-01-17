# Q1. 유효한 팰린드롬 (p.138)

def isPalindrome(str):
    # 초기값 예외처리
    # 1) 대소문자 구분하지 않음
    # 2) 영문자와 숫자만 대상으로 함
    str = str.lower() #대문자가 들어와도 소문자로 만들어버린다.
    if not str.isalnum():
        return False
    isPalin = True

    for i in range((len(str) // 2)):
        j = len(str) - 1 - i;
        if (str[i] != str[j]):
            isPalin = False
            break

    return isPalin

def isPalindrome2(str):
    isPalin = True

    for i in range((len(str) // 2)):
        if (str[i] != str[-i-1]):   #slicing
            isPalin = False
            break

    return isPalin

def isPalindrome3(str):
    isPalin=True

    return isPalin

# 두수의 합
# 덧셈을 하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# input = [2, 7, 11, 15]
# target 9
# output = [0, 1]
def twoSome(nums,target): ## 브루트포스 (완전탐색)
    answer=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                return [i,j]

def twoSome2(nums,target):
    for i,n in enumerate(nums):
        complement = target-n
        if complement in nums[i+1:]: # 기준 + n = target  기준이 원하는 수 = complement  -> complement 가 현재 배열에 기준 뒤에 존재하는가?
            return [nums.index(n),nums[i+1:].index(complement)+(i+1)]  # nums[i+1:] -> 배열의 시작인덱스가 i+1부터 시작이라 뒤에 i+1을 더해줌줌if __name__ == "__main__":
    # mom, rotator, ... 앞이나 뒤에서 읽어도 똑같아.
print(twoSome([6,6],12))
