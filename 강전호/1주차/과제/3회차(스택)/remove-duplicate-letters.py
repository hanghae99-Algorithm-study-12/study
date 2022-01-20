#중복된 문자를 제외하고 사전식 순서(Lexicographical Order)로 나열
#bcabc      ->  abc
#ebcabc     ->  eabc
#eacabce    -?  abce
#cbacdcbc   ->  acdb
#acdb
from collections import Counter


def solution(s):
    counter,seen,stack = Counter(s),set(),[]

    for char in s:
        counter[char]-=1
        if char in seen:
            continue
        #뒤에 붙일 문자가 남아있다면 스택에서제거
        while stack and char<stack[-1] and counter[stack[-1]]>0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)

print(solution("cbacdcbc"))