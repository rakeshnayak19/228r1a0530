fp=open("csea2.txt","w+")
if fp :
    print("file is created sucessfully")

fp.writelines("CMR engineering college\n good morning ")
c=fp.read()
print(c)
fp.close()