####  ARGS

def sum(*args):
    s=0
    for i in args:
        s+=i   #s=s+i   1 2 3 4
    print("sum is ",s)
sum(10,2,3,4,5,7,8)

def three(a,b,c):
    print(a,b,c)
args=[1,2,3]     #list
three(*args)

# ###### KWARGS example 1

def four(a,b,c):
    print(a,b,c)
a={'a':'one','b':'two','c':'three'}
four(**a)


# ###### KWARGS example 1

def fun(**kwargs):                           # * * represents Key and value
    for i,j in kwargs.items():
        print(i,j)
fun(name="tom",sport="football",role=10)
