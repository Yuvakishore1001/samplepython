# __str__

class mystr():
    def __str__(self):
        return "welcome"

c=mystr()
print(c)      #__main__.mystr object at 0x0000025A97B37190(str function returns the memory location



class Emp():
    def __init__(self, ename, eid, esal):
        self.ename = ename
        self.eid = eid
        self.esal = esal

    def __str__(self):
        return("emp name:{} emp ID:{} emp sal:{}".format(self.ename, self.eid, self.esal))
        # return("emp name:%s emp ID:%d emp sal:%g" % (self.ename, self.eid, self.esal))


m1 = Emp("yuva", 100, 1001)
print(m1)