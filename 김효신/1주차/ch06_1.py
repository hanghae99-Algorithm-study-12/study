import collections

def findAnagram():
    array = ["eat", "tea", "tan", "ate", "nat", "bat"]
    new = collections.defaultdict(list)
    for i in range(len(array)):
        str = list(array[i])
        print(sorted(str))
        s = ''.join(sorted(str))
        print(s)
        # new dict의 key 값이 s일 때, 만일 key: s의 값이 없으면 빈 리스트를 도출하고 그 다음은?
        new[s] = new.get(s, []) + [array[i]]
    print(new)


if __name__ == "__main__":
    findAnagram()