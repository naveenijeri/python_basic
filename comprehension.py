##LIST COMPREHENSIONS####
test_list = [1,2,3,4,5,6,7,8,9,10]
# even_list = []
# for i in test_list:
#     if i%2 == 0:
#         even_list.append(i)
# print(even_list)

even_list = [i for i in test_list if i%2 == 0]
print(even_list)

##SET COMPREHENSIONS###
test_set = set([1,2,3,4,5,6,7,8,9,10])
even_set = {i for i in test_set if i%2 == 0}
print(even_set)

##DICTIONARY COMPREHENSIONS###
country = {'india', 'us', 'uk', 'nz'}
city = {'mumbai', 'newyork', 'london', 'livington'}
location_data = zip(country,city)
location_dict = {country:city for country, city in location_data}
print(location_dict)

