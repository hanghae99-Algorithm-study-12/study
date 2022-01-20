# `중복 문자 없는 가장 긴 부분 문자열`
중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.

입력:`"abcabcbb` 출력:`3`  설명 : 정답은 abc로 길이는 3이다.

---

# 내가 푼 코드 
```python
import heapq
from collections import deque

def solution(a):
    temp=[]
    temp=deque(temp)
    answer=[]
    for i in a:         # 들어온 문자열을 돌아간다
        if i not in temp:       #들어온 문자열이 temp에 없다면
            temp.append(i)      #삽입
        else:                   #중복이 된다면

            q =(''.join(temp))      #들어오기 전까지의 문자열로 묶음
            heapq.heappush(answer,(-len(q),q))  #answer에 문자열길이를 음수로 해서 키값으로한다

            while i in temp:        #중복되는 지점 전까지 다 삭제
                temp.popleft()
            temp.append(i)          #중복이 안되니까 삽입



    q = (''.join(temp))     # 마지막에 나온 문자까지 answer에 넣어주고 pop해주면 끝
    heapq.heappush(answer, (-len(q), q))
    #answer에 저장되어있는것중 가장 작은것이 pop되기 때문에 음수로 바까서 저장해주었으니 
    # 다시 -를 해주어 가장 길이가 긴값을 리턴
    return -heapq.heappop(answer)[0]    
a="abcabcbb"
print(solution(a))
```

---
# 답지
```python
def solution(s:str):
    used={}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <=used[char]: # 이미 등장했던 문자라면 START위치 갱신
            start = used[char]+1
        else:
            max_length = max(max_length,index-start+1) #최대 부분 문자열 갱신

        used[char]=index    #현재 문자의 위치 삽입
        print(used)
    return max_length

a="abcabcbb"
print(solution(a))
```

