# def mydecorator(fn):
#     print("mydecorator is called")
#     def inner_func():
#         fn()
#         print("How are you")
#     return inner_func

# @mydecorator
# def greet():
#     print("Hello")

# result = greet()
# print(result)
def zerodivison_check(func):
    def inner_func(arg1, arg2):
        print("My arguments are {}, {}".format(arg1, arg2))
        if arg2==0:
            return "Zerodivision error"
    return inner_func


@zerodivison_check
def division_fun(a,b):
    return a/b
result = division_fun(10,0)
print(result)