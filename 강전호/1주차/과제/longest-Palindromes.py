# 가장긴 팰린드롬 부분 문자열을 출력하라
# 입력
#       "babad"                         "cbbd"
# 출력
#       "bab" or "aba"                  "bb"

input = "asddsasas"

palentrome=""
tempp=""
for i in range(1,len(input)):

    cnt=0
    while True:
        temp = i #1

        left = temp-cnt # 0
        right = temp+cnt#2

        if left<0 or right>len(input)-1:
            left+=1
            right-=1
            tempp=input[left:right+1]
            if len(palentrome)<=len(tempp):
                palentrome=tempp
                print(tempp)
            break

        if (input[left] != input[right]):

            tempp=input[left+1:right]

            if len(palentrome)<=len(tempp):

                palentrome=tempp

            break

        cnt += 1 #cnt=2
print(palentrome)


