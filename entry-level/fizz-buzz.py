value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0: # If value is a multiple of 3 or 5 
    print("FizzBuzz")
elif value % 3 == 0: # If value is a multiple of 3
    print("Fizz")
elif value % 5 == 0: # If value is a multiple of 5
    print("Buzz")
else:
    print(value)