def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0
#a=int(input())
#b=int(input())
print("And")
print(AND(1,1))
print(AND(1,0))
print(AND(0,1))
print(AND(0,0))

def OR(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1
#a=int(input())
#b=int(input())
print("or")
print(OR(1,1))
print(OR(1,0))
print(OR(0,1))
print(OR(0,0))

def XOR(a,b):
    if a!=b:
        return 1
    else:
        return 0
#a=int(input())
#b=int(input())
print ("xor")
print(XOR(1,1))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(0,0))
