list1 = [2,3,4,5,6,7,8,9,2]
for ele in list1:
    if ele%2 == 0:
        list1.remove(ele)
print(list1)

#using list comprehension
[list1.remove(ele) for ele in list1 if ele%2 == 0]
print(list1)