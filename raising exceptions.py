def enterage(age):
    if age < 0:
        raise ValueError("only positive numbers will be allowed")
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
try:
    num=-5
    enterage(num)
except ValueError:    
    print("enter positive number only")
except:
    print("something is wrong")


####
try:
    number=two
    print("the number is :",number)
except NameError as z:
    print("exception is: ",z)



