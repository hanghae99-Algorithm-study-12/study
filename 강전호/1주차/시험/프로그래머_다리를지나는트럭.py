from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [0] * bridge_length
    bridge=deque(bridge)
    truck_weights=deque(truck_weights)

    bridge_weight=0
    while bridge:
        if truck_weights:
            if (bridge_weight-(bridge[-1])+truck_weights[0]<=weight):
                if truck_weights:
                    bridge_weight+=truck_weights[0]
                    bridge.appendleft(truck_weights.popleft())
            else:
                bridge.appendleft(0)
        else:
            bridge_weight-=bridge.pop()
            bridge.append(0)
        bridge_weight -= bridge.pop()
        answer+=1
    return answer
print(solution(100,100,	[10,10,10,10,10,10,10,10,10,10]))
