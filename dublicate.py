#Remove the Dublicate from the list
original_list=[1,2,3,4,2,4,1,2]

import time
#solution 1
def remove_dublicate(original_list):
    unique_elements = []
    for element in original_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements
start_time = time.time()
result = remove_dublicate(original_list)
end_time = time.time()
print(result,"time taken by remove_dublicate is {}".format(end_time-start_time))

#solution2
start_time = time.time()
unique_elements = []
[unique_elements.append(element) for element in original_list if element not in unique_elements] 
end_time = time.time()
print("time taken by using list comprehension{}".format(end_time-start_time))

