t= int(input())
tnum=0
arr=[]
for i in range(0,t):
    n=int(input())
    e=list(map(int,input().split()))
    print(e)
    for j,k in zip(e[0::],e[1::]):
        arr.append((j-k))
    print(arr)





