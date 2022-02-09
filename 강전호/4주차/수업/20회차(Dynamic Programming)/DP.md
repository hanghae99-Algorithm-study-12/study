# 동적 계획법 (Dynamic Programming)

동적 계획법(Dynamic Programming)이란 복잡한 문제를 간단한 
여러 개의 문제로 나누어 푸는 방법을 말한다. 이것은 부분 문제 
반복과 최적 부분 구조를 가지고 있는 알고리즘을 일반적인 방법에 
비해 더욱 적은 시간 내에 풀 때 사용한다.

---

여러 개의 하위 문제를 풀고 그 결과를 기록하고 이용해 문제를 해결하는 알고리즘입니다!

즉, 우리가 재귀함수를 풀어나갈 때 많이 했던 함수의 수식화를 시키면 됩니다.

`F(string) = F(string[1:n-2])` 라고 수식을 정의했던 것 처럼,
문제를 쪼개서 정의할 수 있으면 동적 계획법을 쓸 수 있습니다!

이처럼 문제를 반복해서 해결해 나가는 모습이 재귀 알고리즘과 닮아있습니다!
그러나 다른 점은, 그 결과를 기록하고 이용한다는 점입니다!

여기서 용어정리 간단하게 해드리겠습니다!

결과를 기록하는 것을 메모이제이션(Memoization) 이라고 하고,
문제를 쪼갤 수 있는 구조를 겹치는 부분 문제(Overlapping Subproblem)라고 합니다

---

- 피보나치

![피보나치](https://teamsparta.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F50aa176c-e2aa-4d33-8ff7-c6b463ca9636%2FUntitled.png?table=block&id=ee8b8f00-3d5d-4aa8-90d5-e1e57dc582ae&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=1020&userId=&cache=v2)

```python
memo = {1: 1, 2: 1}


def fibo(n):
    if n in memo:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    print(memo)
    return memo[n]
fibo(10)
```