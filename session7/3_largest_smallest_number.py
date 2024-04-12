# Find the Largest and Smallest Number in a List [10, 20, 5, 40, 30, 72, 34]

numbers = [10, 20, 5, 40, 30, 72, 34]

for number in numbers:
    numbers.sort()

print("The largest number is", numbers[-1], "and the smallest number is", numbers[0])