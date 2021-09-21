print("Hello world...")

# case-sensitive, letters(a-z), underscore, numbers(0-9)
x = 5
y = "Automation"
print(x)
print(y)

print("Hello " + y)

x = 10
y = 20
print(x+y)

if 10 > 5:
    print("10 > 5")

def sum(a,b):
    print(a+b)

x = sum(20,30)

x = 5
y = 2.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

# Casting
x = int(2)    #2
y = int(2.5)  #2
z = float(1)  #1.0
p = str(10)   #"10"

print(x)
print(y)
print(z)
print(p)

x = "Hello World.."
print(x[6:11])

x = "Hello World.."
print(x.upper())

x = "     Hello World..     "
print(x.strip())

x = "     Hello World..     "
print(x.replace("e", "a"))

x = "     Hello,World..     "
print(x.split(","))

print("Enter your name: ")
x = input()
print("Hello, "+x)

