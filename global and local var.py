global_var=150

def fun():
    local_var=200
    print(global_var)

fun()
#######################
xy=100
def fun():

    xy=200
    print(xy)
fun()

print(xy)

########################

t=100

def fun():
    global t
    t=10
    print(t)
fun()

print(t)