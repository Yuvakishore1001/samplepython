start = int(input("enter a start value :"))
end = int(input("enter a end value :"))
def sum(start,end):
    if (start>end):
        print("start should be less than end")
        return  #none
    result=0
    for i in range(start,end+1):
        result=result+i
    print ("Total sum is :",result)


sum(start,end)
# s = sum(start,end)
# print(s)



