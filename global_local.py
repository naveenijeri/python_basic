# Rferences: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# GLOBAL
x = "Global"


def foo():
    global x  # References: https://www.programiz.com/python-programming/global-keyword
    x = x*2
    print("x inside:", x)


foo()
print("x outside:", x)

# LOCAL


def foo():
    y = "Local"
    print(y)


foo()

# NON LOCAL


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
