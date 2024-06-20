
try:
      a=int(input("enter a value"))
      b=int(input("enter b value"))
      c=a/b
      print("c is",c)
except ZeroDivisionError:
    print("cannot divide by zero")#zero division
    #print("b value not given")#value exception
