len("Hello") # len() function only work with Strings

# check datatype
type("Hello") # String
type(123) # int

## example datatype check
print(type('Hello'))
print(type(123))
print(type(1.2))
print(type(False))

# Datatype conversion
int("123") # from string to integer

## example 1
print(int('123')+int('345'));

## incorrect type conversion
""" int("abc") # what number is this supose to be? """

# Excercise
## Own approaching
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

## course aproaching
name_user = input("Enter your name: ")
length_name = len(name_user)

print("Number of letters in your name: " + str(length_name))