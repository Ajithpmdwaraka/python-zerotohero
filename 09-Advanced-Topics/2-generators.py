# Using generators to generate a sequence of numbers

def countdown(n):
    while n > 0:
        yield n
        n -= 1

count = countdown(5)

for num in count:
    print(num)
