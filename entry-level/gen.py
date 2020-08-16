# To demonstrate generators

# Function
def gen_range(stop, start=1, step=2):
    num = start
    while num <= stop:
        yield num
        num += step

for num in gen_range(10):
    print(num)

