languages = ['Python', 'Java', 'JavaScript']
enumerate_prime = enumerate(languages)
print(list(enumerate_prime))

grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
    print(item)

for count, item in enumerate(grocery):
    print("{},{}".format(count, item))

#Advantages of enumeration over list iteration with range
languages = ['Python', 'Java', 'JavaScript']
for i in range(len(languages)):
    print(i, languages[i])
#But, the same thing can be achieved by one simple function without using range and length functions, which can become tricky at times.

#Let us see how Python enumerate makes it less complicated.

List = ["Red", "Green", "Black", "Blue"]
for i, j in enumerate(List):
    print(i, j)

# Fun fact
# With the help of enumerate, we can create a Python Dictionary out of a list very easily. Let us see how:

List = ["Red", "Green", "Black", "Blue"]
Dict= dict(enumerate(List))
print(Dict)

#Enumerating string
String = "Python"
for i, j in enumerate(String):
    print(i, j)