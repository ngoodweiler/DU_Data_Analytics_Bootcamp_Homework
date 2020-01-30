# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length=len(numbers)
    total=0.0
    for number in numbers:
        total += number
    return total / length

# Test your function with the following:
print(str(average([1, 6, 9])))
print(str(average(range(12))))
