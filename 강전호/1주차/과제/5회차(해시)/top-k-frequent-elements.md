# `상위 k 빈도수`
상위 k번 등장하는 요소를 추출하라.

입력 : `nums=[1,1,1,2,2,3], k=2` 출력 : `[1,2]`

---
#내가 푼 풀이
```python
from collections import Counter
import heapq
def Solution(num,k):
    answer=[]
    freqs=Counter(num)
    freqs_heap=[]

    for i in freqs:
        heapq.heappush(freqs_heap,(-freqs[i],i))

    for i in range(k):
        answer.append(heapq.heappop(freqs_heap)[1])
    return answer
```
Counter를 사용하여 문자열의 빈도수로 딕셔너리 생성하여준다음 상위 k개를 뽑아주면 된다.

힙은 키순서대로 정렬 되기 때문에 빈도수를 키로 해준다.
또한 heapq는 최소힙만 지원하기 때문에 음수로 저장해주어야 가장큰값을 뽑아낼수있다.

---
# 답지 해설
```python
from collections import Counter
def Solution(num,k):
    answer=list(zip(*Counter(num).most_common(k)))[0]
    return answer
```
간단하게 most_common(k)를 사용하면 상위k개를 뽑아준다.
또한 zip을 사용하여 묶어주고 *를 사용하여 풀어준다.
---
#알게된 것

- zip()함수는 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 만드는 역할을 한다.
```python
a=[1,2,3,4,5]
b=[2,3,4,5]
c=[3,4,5]
list(zip(a,b))
```
 출력 결과는`[(1,2),(2,3),(3,4),(4,5)]`이다 list를 써준이유는 값을 출력하기 위해서이다.

---

- 아스테리크(*) 는 파이썬에서 언팩이다.

`Counter(num).most_common(k))` -> `[(1,3),(2,2)]`

언팩을 사용:
`list(zip(*Counter(num).most_common(k)))` ->`[(1,2),(3,2)]`


사용하지 않음:`list(zip(Counter(num).most_common(k)))` -> `[((1,3),), ((2,2),)],`

보는것처럼 언팩은 풀어헤치는 것이다.
