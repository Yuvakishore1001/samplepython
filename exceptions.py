#examp 1
print("program is started")

try:
    print(10/10)
    print(10/0)  #ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("entered in to except block-handled expression")

print("program is ended")


#examp 2

# case 1: thrown exception -> except block will execute
# case 2 : not thrown exception -> else block will execute
# case 3 : exception occured ,not occured-> finally block will execute

print("program is started")

try:
    print(10/10)
    print(10/0)  #ZeroDivisionError: division by zero
except TypeError:
    print("entered in to except block-handled type errpr expression")
except ZeroDivisionError:
    print("entered in to except block-handled zero division expression")
else:
    print("entered in else block")
finally:
    print("enterd final block")


print("program is ended")
