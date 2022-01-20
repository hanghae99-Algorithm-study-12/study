# `일일 온도`


 매일의 화씨 온도 리스트를 받아 , 더 따듯한 날을 위해서는 며칠을 기다려야하는 지를 출력.
---
```python
T = [73, 74, 75, 71, 69, 72, 76, 73]
def dailyTemperatures(T):
    stack=[]
    answer = [0]* len(T)
    for i ,j in enumerate(T):
        while stack and j>T[stack[-1]]:
            last = stack.pop()
            answer[last] =i-last
        stack.append(i)
        

    return answer
print(dailyTemperatures(T))
```
# 아이디어
현재의 `인덱스`를 계속 스택에 쌓아 두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스
의 지점의 온도를 비교하여 인덱스의 차이를 정답으로 처리
---
# 과정
1. answer 에 날짜만큼 0으로 배열생성
2. 인덱스와 값으로 for문 돌림
3. 처음에 인덱스를 스택에 삽입
4. 스택이 안비어있고 현재 날씨가 스텍에 있는 날씨보다 따듯하면 스텍에 있는 인덱스를 꺼내와서
5. 인덱스의 차이만큼 답에 저장해준다.

---
# 배운것
```python
a=[100,200,300,400]
for i,j in enumerate(a):
    print(i,j)
```
0, 100

1, 200

2, 300

3, 400

이런식으로 출력됨.
즉 인덱스와 함께 값을 나열해주는 함수이다.

