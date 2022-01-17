# 정규 표현식
# : 문자열 형식을 확인하는 식

# 언제 쓸까요?
# ex) 웹 개발 (010-1234-5678, a@naver.com)

import re
# search(), findall(), split(), sub()
# \w: alphabet + number
# \d: number
# \s: space character

if __name__ == "__main__":
    str = "The rain in Spain"
    x=re.search("^The",str)

    print(x)


