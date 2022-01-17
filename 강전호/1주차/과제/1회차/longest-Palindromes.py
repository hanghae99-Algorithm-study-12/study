# 가장긴 팰린드롬 부분 문자열을 출력하라
# 입력
#       "babad"                         "cbbd"
# 출력
#       "bab" or "aba"                  "bb"

# input = "casacdasdsadc"
#
# palin=""
# tempp=""
# for i in range(1,len(input)):
#
#     cnt=0
#     while True:
#         temp = i #1
#
#         left = temp-cnt # 0
#         right = temp+cnt#2
#
#         if left<0 or right>len(input)-1:
#             left+=1
#             right-=1
#             tempp=input[left:right+1]
#             if len(palin)<=len(tempp):
#                 palin=tempp
#
#             break
#
#         if (input[left] != input[right]):
#
#             tempp=input[left+1:right]
#
#             if len(palin)<=len(tempp):
#
#                 palin=tempp
#
#             break
#
#         cnt += 1 #cnt=2
#
# print(palin)
def longestPalindrome(s):
    def expand(left,right):
        while left >=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]

    if len(s)<2 or s == s[::-1]:
        return s

    result = ""

    for i in range(len(s)-1):
        result= max(result, expand(i,i+1),expand(i,i+2),key=len)
    return result

print(longestPalindrome("asddsa"))


