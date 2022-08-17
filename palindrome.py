
number = int(input())
temp = number
reverse = 0
while number > 0:
    import ipdb
    ipdb.set_trace()
    digit = number % 10
    reverse = reverse*10+digit
    number = number//10
if temp == reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
