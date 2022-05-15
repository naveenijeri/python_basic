import time

######WITHOUT DECORATOR ####################
# def calculate_quabe(numbers):
#     result = []
#     start = time.time()
#     for number in numbers:
#         square_number = number*number*number
#         result.append(square_number)
#     end = time.time()
#     print("time taken by qube function is {}".format(end-start))
#     return result

# def calculate_square(numbers):
#     result = []
#     start = time.time()
#     for number in numbers:
#         square_number = number*number
#         result.append(square_number)
#     end = time.time()
#     print("time taken by square function is {} seconds".format(end-start))
#     return result
# array = range(1,10000000)
# square_result = calculate_square(array)
# quabe_result = calculate_quabe(array)

#######WITH DECORATOR##########
def time_it(func):
    import pdb
    pdb.set_trace()
    start = time.time()
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        end = time.time()
        print("{} took {} seconds".format(func.__name__, end-start))
        return result
    return wrapper

@time_it
def calculate_quabe(numbers):
    result = []
    for number in numbers:
        square_number = number*number*number
        result.append(square_number)
    return result

@time_it
def calculate_square(numbers):
    import pdb
    pdb.set_trace()
    result = []
    for number in numbers:
        square_number = number*number
        result.append(square_number)
    return result
array = range(1,10000000)
square_result = calculate_square(array)
quabe_result = calculate_quabe(array)

#####COMMON USE CASES########################
#####1)LOGGING################################
####2)TIMING#############