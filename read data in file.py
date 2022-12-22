file=open("D:\myfie.txt","r")

# print(file.read())  #read entire content in the file
# print(file.read(5))  #read 10 characters the file    #hello
# print(file.readlines())   #read entire content of the file in the array format [' yuva\n', 'how are you\n']
print(file.readline()) #to read the single line
file.close()

# read using for loop
file=open("D:\myfie.txt","r")

for l in file:
    print(l)

# print(file.readline()) #to read the single line
file.close()
