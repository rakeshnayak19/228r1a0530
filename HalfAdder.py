'''
Approach:
• We take two inputs A and B.
• XOR operation on A and B gives the value of the sum.
• AND operation on A and B gives the value of Carry.
'''


import numpy as np
def half_adder(a,b):
    Sum=np.bitwise_xor(a,b)
    Carry=np.bitwise_and(a,b)
    return Sum,Carry

a=1
b=1
Sum,Carry=half_adder(a,b)
print(Sum,Carry)
