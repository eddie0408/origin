###  Here we are trying to add 2 numbers by help of python 
### In case 1 - when trying to add numbers , python recognize as strings and concatenates the two strings rather than adding the numbers.

x = input("what is x ?  ")
y = input("what is y ?  ")

z = x + y

print(z)

## Now in case 2 we will specify the type of variables. By default python is using them as strings but to add two numbers we have to use int() function.

## case 2

a = input("what is a ? ")
b = input("what is b ? ")

c = int(a) + int(b)

print(c)

## Another way to write above program is below. We can eliminate the variable C because it is used in the next line and will not be used after that so we can save aline and make our code short.

v = int(input("what is the value ?  "))
o = int(input("what is the value ?  "))

print(v+o)


