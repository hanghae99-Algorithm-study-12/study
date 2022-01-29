def bubblesort(lst): # 버블정렬
    iters = len(lst)-1
    for iter in range(iters):
        wall=iters-iter
        for cur in range(wall):
            if lst[cur]>lst[cur+1]:
                lst[cur] , lst[cur + 1] = lst[cur+1],lst[cur]
                print(lst)
    return lst

def selectionsort(lst):
    iters = len(lst)-1
    for iter in range(iters):
        minimum=iter #가장작은값으로 가정
        for cur in range(iter+1,len(lst)):
            if lst[cur]<lst[minimum]:
                minimum=cur
        if minimum!=iter: #가정한값이 가장작은값이 아니라 바꼈을경우
            lst[iter],lst[minimum]=lst[minimum],lst[iter]
            print(lst)
    return lst

def insertionsort(lst):
    for cur in range(1,len(lst)):
        for delta in range(1,cur+1):
            cmp = cur - delta
            if lst[cmp]>lst[cmp+1]:
                lst[cmp],lst[cmp+1]=lst[cmp+1],lst[cmp]
                print(lst)
            else:
                break   #이미 앞은 정렬이 완료되어있는 상태
    return lst

def insertionsort2(lst):
    return lst










print("버블정렬")
lst = [4, 6, 2, 9, 1]
bubblesort(lst)
print()
print("선택 정렬")
lst = [4, 6, 2, 9, 1]
selectionsort(lst)
print()
print("삽입 정렬")
lst = [4, 6, 2, 9, 1]
insertionsort(lst)
print()

