# def func_name(parameter):
#     body

def printHello():
    print("Hello")


printHello()


def printHi(name="John"):
    print("Hi, " + name)


printHi("Serhii")
printHi()


def sum1(a, b, c):
    print(a+b+c)


sum1(10, 20, 30)


def sum2(a, b):
    """this is a function to calculate sum of 2 numbers"""
    return a + b


x = sum2(10, 20)
print(x)
