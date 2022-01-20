# `중복 문자 제거`
중복된 문자를 제거하고 사전식 순서로 나열하라

입력 : `"bcabc"` 출력 : `"abc"`

입력 : `"cbacdcbc"` 출력 : `"acdb"`

---
```python
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
```
# 풀이
만약 현재 문자char가 스택에 쌓여 있는 문자 이고, 뒤에 다시붙일 문자가 남아있다면, 쌓아둔걸 꺼내서 없앤다. cbacdcbcd에서 a가 들어올때, 이미 이전에 들어와있던 c와 b는 제거된다.