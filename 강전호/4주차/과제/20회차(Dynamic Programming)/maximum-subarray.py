# 합이 최대가 되는 연속 서브 배열의 합을 리턴.

def maxsub(lst):        #[-2,1,-3,4,-1,2,1,-5,4]
    sub=[0]*len(lst)    # [0,0,0,0,0,0,0,0,0]
    sub[0]=lst[0]       # [-2,0,0,0,0,0,0,0,0]
    print(sub)
    for i in range(1,len(lst)):#누적해서 더해간다.
        if(sub[i-1]>0): #더해오던값이 양수이면 더하는게 더 커지기 때문에 이득이라 누적합을 계속 해준다.
            sub[i]=sub[i-1]+lst[i] #
            print(sub)
        else: # 음수가 되어버리면 다시 인덱스의 값으로 처음부터 더해나갈 생각.
            sub[i]=lst[i]
            print(sub)
    return max(sub)

def max_kadane(lst):
    best_sum=lst[0]
    current_sum=0
    for i in lst:
        current_sum=max(i,current_sum+i)
        best_sum=max(current_sum,best_sum)
    return best_sum


print(maxsub([-2,1,-3,4,-1,2,1,-5,4]))
print(max_kadane([-2,1,-3,4,-1,2,1,-5,4]))