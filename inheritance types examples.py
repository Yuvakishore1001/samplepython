#########Single inheritance###########

class A():
    def m1(self):
        print("this is class A")
class B(A):
    def m2(self):
        print("this is class B")

a=A()
a.m1()

b=B()
b.m1()
b.m2()

# b=B()

# ///////////////////////////
class A():
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

b=B()
b.m1()
b.m2()

#########multi level inheritance###########

class A():
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
class C(B):
    c,d=1,2
    def m3(self):
        print(self.c+self.d)


b=B()
b.m1()
b.m2()

c=C()
c.m1()
c.m2()
c.m3()

#########hierarchical inheritance###########\\

class A():
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
class C(A):
    c,d=1,2
    def m3(self):
        print(self.c+self.d)


b=B()
b.m1()
b.m2()

c=C()
c.m1()

c.m3()

######### multiple inheritance###########


class A():
    x,y=1000,2000
    def m1(self):
        print(self.x+self.y)
class B():
    a,b=100000,200000
    def m2(self):
        print(self.a+self.b)
class C(A,B):
    c,d=11,22
    def m3(self):
        print(self.c+self.d)

a=A()
a.m1()

b=B()
b.m2()

c=C()
c.m1()
c.m2()
c.m3()