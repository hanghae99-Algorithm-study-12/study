import bisect


def findnum(lst, target):
    left = bisect.bisect_left(lst, target)
    right = bisect.bisect_right(lst, target)

    if not (0 <= left < len(lst) and lst[left] == left):
        return -1

    return right - left


print(findnum([1, 1, 2, 2, 2, 2, 3], 4))
