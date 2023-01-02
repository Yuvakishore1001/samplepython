### ABC is a predefined abstract class
from abc import ABC,abstractmethod
class hello(ABC):
    @abstractmethod
    def display(self):
        None
class B(hello):
    def display(self):
        print("this is display method")

a=B()
a.display()


##################



from abc import ABC,abstractmethod
class fun(ABC):     #Abstarct class
    @abstractmethod
    def m1(self):
        print("Hello M1")
    @abstractmethod
    def m2(self):
        print("Hello M2")
class fun1(fun):
    def m1(self):
        print("hi M1")
class fun2(fun1):
    def m2(self):
        print("Hi M2")

y=fun2()
y.m1()
y.m2()

#####creating a constructor in abstract class###

from abc import ABC,abstractmethod
class X(ABC):
    def __init__(self,value):
        self.value=value
    @abstractmethod
    def add(self):
        pass
    def sub(self):
        pass
class Y(X):

    def add(self):
        print(self.value+100)
    def sub(self):
        print(self.value-10)

y=Y(100)
y.add()
y.sub()

