'''
We take three inputs A ,B and C-in .
• Applying C-IN XOR (A XOR B ) gives the value of sum
• Applying A B + B C + A  gives the value of C-
'''

import numpy as np
def FullAdder(a,b,c):
    sum=c ^ (a ^ b)

    c_out=((a ^ b) and c) or (a and b)
    #print("sum=",sum)
    #print("c_out",c_out)
    print(sum," ",c_out)
#a=0
#b=0
#c=1
#FullAdder(a,b,c)

print("sum  c_out")
FullAdder(0,0,0)
FullAdder(0,0,1)
FullAdder(0,1,0)
FullAdder(0,1,1)
FullAdder(1,0,0)
FullAdder(1,0,1)
FullAdder(1,1,0)
FullAdder(1,1,1)

