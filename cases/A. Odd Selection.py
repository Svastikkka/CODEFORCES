num=int(input())
even_count=0
odd_count=0

for i in range(num):
    m, n = list(map(int, input().split()))
    arr=list(map(int,input().split()))
    a=[]#even once
    b=[]#odd ones

    for j in range(len(arr)):

        if arr[j]%2==0:
            a.append(arr[j])
            even_count+=1
        else:
            b.append(arr[j])
            odd_count+=1
    print(a)
    print(b)
    res=0
    if odd_count==0:
        print("No")
    else:
        if len(b)%2==0:
            print(sum(b[1:]))
        else:
            print(sum(b))














