T=int(input())
for i in range(0,T):
    num=int(input())
    for j in range(1,num+1):
        if j%2 == 0:
            print("-----------",j)
        else:
            print(j)