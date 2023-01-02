def display():
    print("this is from module1")

class emp():
    def __init__(self,empid,empname,sal):
        self.empid=empid
        self.empname=empname
        self.sal=sal
    def display(self):
        print("empid:{} empname:{} empsal:{}".format(self.empid,self.empname,self.sal))
