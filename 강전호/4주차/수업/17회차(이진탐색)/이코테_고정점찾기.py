def fixed(lst):
    left = 0
    right=len(lst)

    while left<right:
        mid=(left+right)//2

        if lst[mid]<mid:
            left = mid+1
        else:
            right = mid
    if (left>=len(lst) or (left!=lst[left])):
        return -1
    return left

print(fixed([-15,-6,1,3,7]))