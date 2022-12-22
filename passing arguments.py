

#positional arguments
def fun(i,j=100):
    print(i,j)

fun(50)   #50 100   positional parameters

fun(100,250)  #250 will go anďsit in the already allocated value of j

# keyword  arguments

def named_arg(name,greetings):
    print(greetings," ",name)

named_arg("yuva","hi")   #positional arguments
named_arg(name="yuva",greetings="hi")   #key word arguments
named_arg(greetings="hi",name="yuva")   #key word arguments

def fun(a,b,c):
    print(a,b,c)
fun(10,20,30)
fun(10,b="20",c="30")
fun(10,c="30",b="20")
fun(10,b="20",c="30")  #positional arguments must be passed first



