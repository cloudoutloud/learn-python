# This script, takes a user input Fahrenheit value and converts in to celsius rounding it to 2 decimal place.

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
celsius = (fahrenheit - 32) * 5 / 9 
print(fahrenheit, "F is converted to", round(celsius, 2), "C")