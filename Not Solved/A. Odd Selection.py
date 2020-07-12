num=int(input())
for i in range(num):
    m, n = list(map(int, input().split()))
    sum = 0
    arr=list(map(int,input().split()))
    for j in range(n):
        if len(arr)==1 and m==1 and n>0:
            sum=sum+arr[0]
        elif len(arr)>1 and n==1:
            sum=sum+arr[0]
        elif n<1:
            print("NO")
        else:
            sum=sum+arr[j]
    if sum%2==0:
        print("No")
    else:print("Yes")






