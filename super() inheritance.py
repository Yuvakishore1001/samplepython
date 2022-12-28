
#calling the class method using super()

class A:
    def m1(self):
        print("Hello A")
class B(A):
    def m2(self):
        super().m1()   #calling parent method using SUPER()
        print("hello B")
b=B()
b.m2()

#calling the Variables using super()

class A:
    x,y=10,20

class B(A):
    a, b = 100, 200
    def m2(self,i,j):
        # super().m1(a,b)   #calling parent method using SUPER()
        print(i+j)              #local varaiable
        print(self.a+self.b)    #child class variable
        print(self.x+self.y)    #parent class variable
b=B()
b.m2(1,2)

#calling the same (a,b) Variables using super()


a,b=15,20
class A:
    a,b=10,20

class B(A):
    a, b = 100, 200
    def m2(self,a,b):
        # super().m1(a,b)   #calling parent method using SUPER()
        print(a+b)              #local varaiable
        print(self.a+self.b)    #child class variable
        print(super().a+super().b)    #parent class variable using super
        print(globals()['a'] + globals()['b'])    #calling global variables
x=B()
x.m2(1,2)


# ####### calling constructor using super()

class A:
    def __init__(self):
        print("this is from class A")
        
class C:
    def __init__(self):
        print("this is from class C")

class B(A,C):
    def __init__(self):
        print("this is from class B")
        super().__init__()    #1 way of calling parent class constructor
        A.__init__(self)       ##another way of calling parent class constructor
        C.__init__(self)
b=B()


