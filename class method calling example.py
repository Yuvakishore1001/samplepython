class Emp():
    def __init__(self, ename, eid, esal):
        self.ename = ename
        self.eid = eid
        self.esal = esal

    def display(self):
        print("emp name:{} emp ID:{} emp sal:{}".format(self.ename, self.eid, self.esal))
        print("emp name:%s emp ID:%d emp sal:%g" % (self.ename, self.eid, self.esal))


m1 = Emp("yuva", 100, 1001)
m1.display()

# class Emp():
#     def __init__(self,ename,eid,esal):
#         self.ename = ename
#         self.eid = eid
#         self.esal = esal
#     def display(self):
#         print("emp name:{} emp id:{} emp sal:{}".format(self.ename,self.eid,self.esal))
#         print("emp name:%s emp ID:%d emp sal:%g" % (self.ename, self.eid, self.esal))
#
# m1 = Emp("yuva",1001,1000)
# m1.display()