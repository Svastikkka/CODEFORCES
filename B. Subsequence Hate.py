import re

def trailing_zeros(longint):
    manipulandum = str(longint)
    return len(manipulandum)-len(manipulandum.rstrip('0'))
def trailing_ones(longint):
    manipulandum = str(longint)
    return len(manipulandum)-len(manipulandum.rstrip('1'))

num=int(input())
for i in range(num):
    b=input()
    x = re.search("^1(0+)1$", b)
    y = re.search("^0(1+)0$", b)
    if x :
        print(trailing_zeros(int(x)))
        print(trailing_ones(int(x)))

    if y:
        print(2)
