N,M=map(int,(input().split()))
note={}
for i in range(N):
    address,password=map(str,(input().split()))
    note[address]=password

for i in range(M):
    address=str(input())
    print(note[address])