T=list(map(int,input().split()))
special_character="!()-[]{};:'\"\,<>./?@#$%^&*_~"
r=""
for i in range(0,T[0]):
    word=list(map(str,input().split(" ")))

    for j in range(0,len(word)):

        x=word[j][0].replace("-","").replace("@","").replace("$","").replace("^","").replace("&","").replace("*","").replace("[","").replace("]","").replace("{","").replace("}","").replace("&","")
        y=word[j][1:].replace("-","").replace("@","").replace("$","").replace("^","").replace("&","").replace("*","").replace("[","").replace("]","").replace("{","").replace("}","").replace("&","")
        result=y+x+"ay "
        r=r+result
    print(r.capitalize())



