# `보석과 돌`
J는 보석이며 S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

입력 : `J="aA"  S="aAAbbbb`
출력 : `3`

---
```python
from collections import Counter

J='aA'
s="aAAbbbb"

s=(Counter(s)) #counter를 이용하여 s={'b': 4, 'A': 2, 'a': 1}로 저장

answer=0
for i in J: # stone안에 보석이 있으면 answer+=보석수
    answer+=s[i]
print(answer)
```
---
# 문제풀이
간단한 문제였다. 
s를 Counter을 이용하여 빈도수가 나오는 딕셔너리로 저장한후 보석인것을 찾아 answer에 더해주면서 해결.

---
# 알게된 것
파이썬에서 제공하는 `collections` 모듈의 `Counter`클래스를 사용하면 데이터의 개수를 셀때 유용하다.
- `Counter(list)`: 문자열이나 list의 요소를 카운팅하여 많은 순으로 딕셔너리 형태로 리턴한다.
- `most_common()` : 개수가 많은 순으로 정렬된 튜플 배열 리스트를 리턴해준다.
  - `most_common(k)`를 사용하면 k개 만큼 보여준다.