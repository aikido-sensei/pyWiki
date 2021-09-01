"""
paradigms: object oriented, functional
class, function/routine,

# Datatypes - https://www.w3schools.com/python/python_datatypes.asp

"""

# string
strValue = "Isaac"

print(strValue)
print(type(strValue))

# int
intValue = 15

print(intValue)
print(type(intValue))

# float
floatValue = 15.15

print(floatValue)
print(type(floatValue))

# complex
complexNumberValue = complex(2.3, 4.0)
print(complexNumberValue)
print(type(complexNumberValue))

# list - mutable type
listOfValues = [1, 2, 3]
print(listOfValues)
listOfValues.append(4)
print(listOfValues)
list2 = [7, 8, 9]
newList = listOfValues + list2
print(newList)
newList += [100]
print(newList)

# list is pass by reference
list1 = [1, 2, 3]
list1[0] = 10
list2 = list1 # To make them separate, use list2 = list(list1)
list2 += [4]
print(list1)
print(list2)
for element in list2:
    print(element)

#for index in list2:
    #print(list2[index])

#for index, element in enumerate(list2):
    #print(index + ": " + element)

#list3 = [[1,2,3],[4,5,6]]
#for index1 in list3:
    #for index2 in range(len(list3[index1])):
        #print(list3[index1][index2])

# tuple - immutable type
tuple1: tuple = (1, 2, 3)
tuple2 = (4, 5, 6)
# tuple1[0] = 10 # Cannot do this as tuple is immutable.
print(tuple1)
tuple3 = tuple1 + tuple2
tuple3 += tuple1 # tuple3 = tuple3 + tuple1
tuple3 = tuple3 + (10,)
tuple4 = tuple3
print(tuple3)

#Boolean True/False
boolean1 =True
boolean2 = False

print(boolean1)
print(type(boolean1))

dict1 = {
    "key1": 1,
    "key2": 2,
}


