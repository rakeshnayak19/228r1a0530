class A:
    def method(self):
        print("A class is defined")
        super().method()
class B:
    def method(self):
        print("B class is defined")
        super().method()
class c(B,A):
    def method(self):
        print("c class")
        super().method()
obj=c()
obj.method()