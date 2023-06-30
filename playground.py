# Experiment with functions that take multiple arguments
def add(*args):
    total = 0
    for num in args:
        total = total + num

    return total


sum = add(5, 6, 10, 20, 5)
print(sum)
