num=int(input())
state=0
for i in range(num):
    n=int(input())
    s=list(map(int,input().strip()))
    if sorted(s) == s:
        print(s)
    else:
        for j in range(len(s)-1):
            print(j)
            for k in range(len(s)-1):
                if s[k]==1 and s[k+1]==0:
                    s.remove(s[k])
                    s.remove(s[k+1])


                print(s[k],s[k+1])


