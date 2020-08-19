x,y=map(int,input().split())
arr=list(map(int,input().split()))
res=sorted(arr,reverse=True)
sum=0
for i in range(len(res)):
    if sum<y:
        sum=sum+res[i]
    else:
        print(i)
        break

