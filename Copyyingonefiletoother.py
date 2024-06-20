fp1=open("csea.txt","r")
fp2=open("csea1.txt","w+")
if fp1:
    print("opened successfully")
for i in fp1:
    fp2.write(i)
print("file is copied successfully ")
fp2.seek(0,0)
c=fp2.read()
print(c)
fp1.close()
fp2.close()