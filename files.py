'''
 1.open()
 2.close()
 3.read()
 4.readline()
 5.write()
 6.writeline()
 7.seek()
 8.tell()
'''
fp=open("csea.txt","w+")
if fp :
    print("file is created sucessfully")

fp.writelines("CMR engineering college\n good morning ")
c=fp.read()
print(c)
fp.close()