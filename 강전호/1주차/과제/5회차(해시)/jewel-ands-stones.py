from collections import Counter

J='aA'
s="aAAbbbb"

s=(Counter(s)) #counter를 이용하여 s={'b': 4, 'A': 2, 'a': 1}로 저장

answer=0
for i in J: # stone안에 보석이 있으면 answer+=보석수
    answer+=s[i]
print(answer)