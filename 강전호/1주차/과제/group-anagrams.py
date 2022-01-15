# 문자열 배열을 받아 애너그램 단위로 그룹핑 하라
# 입력
#       ["eat", "tea", "tan", "ate", "nat", "bat"]
# 출력
#       [
#           ["ate","eat","tea"],
#           ["nat", "tan"],
#           ["bat"]
#       ]
import collections

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams={}
for i in input:
    try:
        anagrams["".join(sorted(i))].append(i)
    except KeyError:
        anagrams["".join(sorted(i))] = [i]

print(list[anagrams.values()])


