fp=open("csea2.txt","r")
words=0
for i in fp:
    i=fp.read()
    lines=i.split(" ")
    words +=len(lines)
print(len(words))