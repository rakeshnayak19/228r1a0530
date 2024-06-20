fp1=open("csea.txt","r")
if fp1:
    print("created successfully")
    fp1.seek(0, 0)
    for i in fp1:
         print(i)

'''c=fp1.readline()
print(c)
c=fp1.readline()
print(c)
fp1.close()'''