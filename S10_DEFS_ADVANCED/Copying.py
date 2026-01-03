import copy

"""" copy - płytka """

def evil_function(ToBeDestroyedList):
    print (id(ToBeDestroyedList))
    ToBeDestroyedList[0] = 20
    print(ToBeDestroyedList)

myList = [1,4,2,1,52,3]

print (id(myList[0]))
evil_function(myList[:])

a = 4
b = 4 # INT immutable

print (myList)