#### OVER RIDING#####

class parent():
    name="yuva"

class child(parent):
    pass
    # name="kishore"

obj=child()

print(obj.name)


#########################

class bank():
    def rateofinterest(self):
        return 0
class icici(bank):
    def rateofinterest(self):
        return 10.5

obj=icici()

print(obj.rateofinterest() )

obj1=bank()
print(obj1.rateofinterest())



##### OVER LOADING #######
###example 1
class fun():
    def hello(self,name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")

a=fun()
a.hello(" yuva")
a.hello()



##### OVER LOADING #######
###example 2

class bird():
    def fly(self,name=None):
        if name=="parrot":
            print("parrot can fly")
        if name=="penguin":
            print("penguin cannot fly")
        if name==None:
            print("No input")
a=bird()
a.fly("parrot")
a.fly("penguin")
a.fly()
