t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    count0=arr.count(0)
    count1=arr.count(1)

    if count0>=n//2:
        print(count0)
        for i in range(count0):
            print(0,end=" ")
    else:
        print(count1-(count1%2))
        for i in range((count1-(count1%2))):
            print(1,end=" ")
    print()

    t=t-1

