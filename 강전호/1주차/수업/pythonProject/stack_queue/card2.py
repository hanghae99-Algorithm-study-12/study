from collections import deque

def get_card(num):
    queue = deque([n for n in range(1,num+1)])
    while len(queue)>1:
        # 1. 일단 카드를 버린다.
        front = queue.popleft()
        # 2. 그다음 제일 위 제일 뒤로 옮긴다.
        queue.append(queue.popleft())
        # 3. 한장 남은 카드를 반환한다.
    return queue.popleft()

assert get_card(6) ==4