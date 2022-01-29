a=[3,30,34,5,9]
def insertionsort(lst):
    for cur in range(1,len(lst)):
        for delta in range(1,cur+1):
            cmp = cur - delta
            if str(lst[cmp])+str(lst[cmp+1])<str(lst[cmp+1])+str(lst[cmp]):
                lst[cmp],lst[cmp+1]=lst[cmp+1],lst[cmp]
            else:
                break
    return str(int(''.join(map(str,lst))))

print(insertionsort(a))