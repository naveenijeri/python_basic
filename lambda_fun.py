#Lambda function is anonymous function it takes as any number of arguments and one expression##
from tkinter import N


a = lambda x: x*2
print(a(2))

#lambda function is using another function

def my_function(n):
    return lambda x : x*n

mydoubler = my_function(2)

print(mydoubler(11))
