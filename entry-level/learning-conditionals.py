name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is long")
elif len(name) == 5:
    print("your name is 5 characters")
elif len(name) >= 4:
    print("your name is greater than 4 characters")
else:
    print("your name is short")