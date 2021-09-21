class MyClass:
    name = 'Serhii'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)


x = MyClass("Max", 30)
print(x.name)
x.sum(4, 5)
del x.name
print(x.age)
