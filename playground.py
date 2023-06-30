# Experiment with functions that take multiple positional arguments
def add(*args):
    total = 0
    for num in args:
        total = total + num

    return total


sum = add(5, 6, 10, 20, 5)
print(sum)

# experiment with function that take multiple key word argurments


def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiple"]

    return n


print(calculate(7, add=10, multiple=15))
