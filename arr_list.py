#differences between python array and list
#Arrays in python can only contain elements of same data types i.e., data type of array should be homogeneous and consumes far less memory than lists.
#Lists in python can contain elements of different data types i.e., data type of lists can be heterogeneous. It has the disadvantage of consuming large memory.

import array
# print(dir(array))
# print(array.__doc__)
a = array.array('i',[1,2,3,])
# a = array.array('i',[1.0,2.3,3.456,])
print(a)
for i in a:
    print(i)