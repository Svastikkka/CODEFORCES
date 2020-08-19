h=int(input())
m=int(input())
s=int(input())
a=input()
if a=="AM":
    print(3600*h+m*60+s)
else:
    print(3600*(h+12)+m*60+s)
