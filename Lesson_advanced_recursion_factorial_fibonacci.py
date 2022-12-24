def privet(x):
    if x == 0:
        return
    else:
        print("Hello World")
        privet(x - 1)


privet(1)


def sum(x):
    if x == 0:
        return 0;
    elif x == 1:
        return 1;
    else:
        return x + sum(x - 1)


i = sum(4)
print(i)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(4))


def Fibonacci(z):
    if z == 0:
        return 0
    if z == 1:
        return 1
    else:
        return Fibonacci(z - 1) + Fibonacci(z - 2)


print(Fibonacci(40))
