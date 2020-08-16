# To demonstrate python scopes

if 1 < 2:
    x = 5 # variable defined top level scope is used in whole script

while x < 6:
    print(x)
    x += 1

print(x)

# With functions vairiables are defined in the own scope
def set_x():
    x = 5

set_x()

while x < 6:
    print(x)
    x += 1

print(x)