number = int(input("Enter the number"))
smallest_divisor = None
for i in range(2, number):
    if number % i == 0:
        if smallest_divisor is None:
            smallest_divisor = i
        else:
            if i < smallest_divisor:
                smallest_divisor = i
print("smallest divisor is {}".format(smallest_divisor))
