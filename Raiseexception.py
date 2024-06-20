try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    if b == 0:
         raise print("cannot be divide by zero")
    else:
        print(a/b)