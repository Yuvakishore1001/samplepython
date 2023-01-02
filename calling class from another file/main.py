###Approach 1

import a
import b

obj=a.animal()
obj.display()

obj1=b.bird()
obj1.display()

###Approach 2

from a import *
from b import *

obj=animal()
obj.display()

obj1=bird()
obj1.display()

##############

import a

print(dir(a))