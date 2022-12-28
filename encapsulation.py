class myclass():
    __a=10
    def hello(self):
        print(self.__a)
obj=myclass()
obj.hello()

# print(myclass().__a)  #cannot be accessed because it is in private

######################

class   myclass():
    def __display(self):      ########this is private method

        print("this is display private method")
    def display(self):

        print("this is public")
        self.__display()
obj=myclass()
obj.display()


#### Access Private variables outside of the class indirectly using methods

class myclass():
    __empid=1001
    def getempid(self,eid):
        self.__empid=eid

    def disempid(self):
        print(self.__empid)

a=myclass()
a.getempid(1005)
a.disempid()