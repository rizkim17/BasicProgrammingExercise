# Remove Duplicates from a List: [1, 2, 3, 4, 2, 3, 5, 6, 1]

list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
nondupelist = []

for numbers in list:
    if numbers not in nondupelist:
        nondupelist.append(numbers)

print (nondupelist)