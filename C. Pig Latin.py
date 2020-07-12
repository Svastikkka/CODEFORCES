


T=int(input())
for i in range(T):
    s=input().split()
    s1=s[0]
    print(s1[1].upper()+s1[2:]+s1[0].lower()+"ay",end=" ")
    s2=s[1:]
    for k in range(len(s2)):
        print(s2[k][1:]+s2[k][0]+"ay",end=" ")
    print()



#############################################################


def word(x):
    first = x[0].lower()
    add = x + first + "ay"
    return add[1::]


T=int(input())
for i in range(T):
    s=input().split()
    s1=list(map(word, s))
    pig_latin = " ".join(s1)
    print(pig_latin[0].upper()+pig_latin[1:])



