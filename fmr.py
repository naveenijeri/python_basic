from functools import reduce
#Filter, Map, Reduce Function
nums = [1,2,3,4,5,6,7,8,9,10]

#Filter function without lambda
def is_even(number):
    return number%2 == 0
even_list = list(filter(is_even,nums))

#Filter function with lambda
even_list = list(filter(lambda n: n%2 == 0, nums))
# print(even_list)

#Map function without lambda
def list_double(number):
    return number*number
double_list = list(map(list_double,nums))
# print(double_list)

#map function with lambda
double_list = list(map(lambda n:n*2,nums))
# print(double_list)

#Reduce function without lambda
def add_all(a,b):
    return a+b

sum_all = reduce(add_all,nums)
print(sum_all)