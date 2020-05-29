x,n=list(map(int,input().split()))
h=list(map(int,input().split()))

coins_collected=0
count=0
for i in range(0,len(h)):
    if coins_collected <n:
        coins_collected=coins_collected+max(h)
        h.remove(max(h))
        count=count+1

    else:
        break

if n%2==0:
    if coins_collected<n:
        print(-1)
    else:print(count)
else:
    if coins_collected<n:
        print(-1)
    else:print(count+1)