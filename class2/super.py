class A:
     def add(self, x):
         y = x+1
         print(y)
class B(A):
    def add(self, x):
        # super().add(x)
        y = x+1
        print(y)
b = B()
b.add(2)
a = A()
a.add(1)