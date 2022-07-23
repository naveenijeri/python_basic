#differences between python array and list
#Arrays in python can only contain elements of same data types i.e., data type of array should be homogeneous and consumes far less memory than lists.
#Lists in python can contain elements of different data types i.e., data type of lists can be heterogeneous. It has the disadvantage of consuming large memory.

# Lists are slightly faster than sets when you just want to iterate over the values.
# Sets, however, are significantly faster than lists if you want to check if an item is contained within it. They can only contain unique items though.
# It turns out tuples perform in almost exactly the same way as lists, except for their immutability.
import array
# print(dir(array))
# print(array.__doc__)
# a = array.array('i',[1,2,3,])
# a = array.array('i',[1.0,2.3,3.456,])
# print(a)
# for i in a:
#     print(i)

#find the count of array elements which matching sum of digits is equal to k
# numbers = [99, 91, 25, 23, 45, 54, 342]
# k = 9
# def find_count(numbers, k):
#     count = 0
#     for number in numbers:
#        number_str = str(number)
#        number_sum = 0
#        for s in number_str:
#            number_sum += int(s)
#        if number_sum == k:
#           count += 1
#     return count
          
           
    
# result = find_count(numbers, k)
# print(result)

#Find the second max element of the list
input_lst = [1,2,3,4,5,6,7,7,9]
def second_max(input_lst):
    max_input_lst = max(input_lst)
    result = None
    for ele in input_lst:
        if not result:
            result = ele
        else:
            if ele>result and ele!=max_input_lst:
                result = ele
    return result
result = second_max(input_lst)
print(result)