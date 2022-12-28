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
