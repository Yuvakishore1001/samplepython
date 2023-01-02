import sys

from pack1.pack2 import module22

sys.path.append("C:/Users/yuvak/PycharmProjects/pythonProject1/pack1");

#approach1

import module1
import module2

module1.display()
module2.show()

#approach2

from module1 import *
from  module2 import *

display()
show()




###############################
# example 2:

# importing modules from 2 diff packages
import sys
sys.path.append("C:/Users/yuvak/PycharmProjects/pythonProject1/pack1");

from module1 import *

import  sys
sys.path.append("C:/Users/yuvak/PycharmProjects/pythonProject1/pack1/pack2");

from module22 import *

module1.display()
module22.show()

#importing classes from diff packages

import sys
sys.path.append("C:/Users/yuvak/PycharmProjects/pythonProject1/pack1")

from module1 import emp

e=emp(101,"yuva",10000)
e.display()

import sys
sys.path.append("C:/Users/yuvak/PycharmProjects/pythonProject1/pack1/pack2");

from module22 import stu

s=stu(1001,"yuva","A")
s.display()

