# This script pulls user data and prints as a string

name = input("What is your name? ")
color = input("What is your favorite colour? ")
age = int(input("How old are you today? "))

# Use end=" " to place print all on same line 
# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")
# print("and loves the color " + color + ".", end=" ")

print(name, 'is', age, 'years  old and loves the color', color + '.', sep=", ")
