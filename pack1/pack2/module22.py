def show():
    print("this is from module22")

class stu():
    def __init__(self,sid,sname,grad):
        self.sid=sid
        self.sname=sname
        self.grad=grad
    def display(self):
        print("sid:{} sname:{} sgrad:{}".format(self.sid,self.sname,self.grad))