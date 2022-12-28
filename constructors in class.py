class myclass():
    def myfun(self):
        print("good Morning")
    def __init__(self):
        print("Hello")
c=myclass()
c.myfun()

#######################################

# val1 = int(input("enter a value :"))
# val2 = int(input("enter a value :"))

class myclass():

    def fun(self,val1,val2):
        val1 = int(input("enter a value :"))
        val2 = int(input("enter a value :"))
        print(val1)
        print(val2)

        self.val1=val1
        self.val2=val2

    def fun2(self):
        print(self.val1+self.val2)
mc=myclass()
mc.fun(val1="val1",val2="val2")
mc.fun2()

###########     OR         #################

class myclass():
    val1 = int(input("enter a value :"))
    val2 = int(input("enter a value :"))
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2
    def fun2(self):
        print(self.val1+self.val2)
mc=myclass()
mc.fun(val1="val1",val2="val2")
mc.fun2()




num=int(input("Enter a number:"))
for i in range(1,10+1):
    print(num,"*",i,"=",num*i)