r=int(input("enter row"))
c=int(input("enter column"))
A=[]
for i in range(r):
    x=[]
    for j in range(c):
        x.append(int(input(f"Enter element at position ({i+1},{j+1}): ")))
    A.append(x)

print("The matrix is:")
for i in range(r):
    for j in range(c):
        print(A[i][j], end=" ")
    print()