import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n= int(input())
    phone=[input().strip() for _ in range(n)]
    phone.sort()
    check=True

    for i in range(n-1):
        long = len(phone[i])
        if phone[i] == phone[i+1][:long]:
            check=False
            break

    if check:
        print("YES")
    else:
        print("NO")