
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



