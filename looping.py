import math

print("loops and data-types")
data_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for i in data_list:
    print(i, type(i))

print("\nFactorials")
n = 5
print("Factorial of", n, "is", math.factorial(n))
