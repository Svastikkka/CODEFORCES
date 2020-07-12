z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def GetColumnNumber(s):

    i=0
    j=""
    for n in s:
        if n.isalpha():
            k= z.index(n)+1
            i=i*26+k
        else:
            j=j+n
    return "R"+j+"C"+str(i)

def GetColumnAlpha(n):

    s = ''
    while n > 0:
        if n % 26 == 0:
            n = n / 26 - 1
            s += 'Z'
        else:
            k = n % 26
            n = n // 26
            s += z[round(k) - 1]

    return s[::-1]



num=int(input())
i=0
while i <num:
    s=input()
    if s[0]!="R":
        print(GetColumnNumber(s))
    else:
        print(GetColumnAlpha(int(s[s.index("C")+1:]))+(s[s.index("R")+1:s.index("C")]))
    i+=1