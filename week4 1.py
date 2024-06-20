def sortedd(li):
    for i in range(len(li)-1):
        if li[i]==li[i+1]:
            return True
        else:
            return False
li1=[1,3,4,2,5,3]
print(sortedd(li1))