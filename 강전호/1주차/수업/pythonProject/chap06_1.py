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
if __name__ == "__main__":
    # mom, rotator, ... 앞이나 뒤에서 읽어도 똑같아.
    print(isPalindrome("bb"))
