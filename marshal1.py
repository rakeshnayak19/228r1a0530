import marshal
s='''
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


n = int(input())
print((fact(n)))
'''
code=compile(s,"s","exec")
fp=open("marshal1.txt","wb")
marshal.dump(code,fp)
fp.close()