def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)


#USAGE#####
#it returns one element each time , it won't return all the elements so memory usage if efficient.