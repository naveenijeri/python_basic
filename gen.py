#refer: https://www.programiz.com/python-programming/generator
#Iterators and Generators
#Iterators: An iterator is an object that contains a countable number of values.
#example: Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# def simpleGeneratorFun():
#     yield 1            
#     yield 2            
#     yield 3            
   
# # Driver code to check above generator function
# for value in simpleGeneratorFun(): 
#     print(value)


#USAGE#####
#it returns one element each time , it won't return all the elements so memory usage if efficient.

a = ["apple", "orange", "banana"]
print(dir(a))