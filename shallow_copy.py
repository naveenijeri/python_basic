#shallow copy creates the a new objects which stores the reference of the original objects
import copy
list1 = [1,[2,3],4,5,6]
list2 = copy.copy(list1) 
print(list1)
print(list2)

print("after changing the list2 nested list")

list2[1][0] = "naveen"
print(list1)
print(list2)

#it will change the original list and referenced list