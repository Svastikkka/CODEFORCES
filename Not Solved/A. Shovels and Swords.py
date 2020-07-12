num=int(input())
for i in range(num):
    s,d=list(map(int,input().split()))
    if s == d:
        print(s//2)
        continue
    count=0
    while s!=0 and d!=0 :
        if s>=d:
            s=s-2
            d=d-1
            count+=1
        elif s<=d:
            d=d-2
            s=s-1
            count+=1
    print(count)

