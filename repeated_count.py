test_list =[1,2,3,4,4,4,3,2,3,3,4]

#Solution 1
repeated_info = {}
for element in test_list:
    repeated_count = test_list.count(element)
    repeated_info[element] = repeated_count
print(repeated_info)
result = max(repeated_info, key=repeated_info.get)
print(result)

#solution 2
repeated_info = { element: test_list.count(element) for element in test_list}
result = max(repeated_info, key=repeated_info.get)
print(result)

