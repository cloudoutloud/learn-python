# This script indexes and slices characters from a user input string

message = input("Enter a message: ")
print("First Character:", message[0]) 
print("Last Character:", message[-1])
print("Middle Character:", message[int(len(message) / 2)])
print("Even Character:", message[0::2]) # Starts at 0 characeter and jumps 2
print("Odd Character:", message[1::2]) # Starts at 1 characeter and jumps 2 
print("Reversed message:", message[::-1])
