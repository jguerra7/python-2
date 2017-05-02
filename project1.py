#hello world
x = "hello world"
print x


#error handling
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1/num2
except ValueError:
    print("Two numbers are required.")
except ZeroDivisionError:
    print("Denominator can't be a zero.")
else:
    print(num1, "/", num2, "=", result)


#functions
def square(x):
    return x * x

for y in range(1, 11):
    print (square(y))


#fizzbuzz
maxFizzBuzz = int(input("Enter max number")) + 1

for y in range(1, maxFizzBuzz):
    if y % 3 == 0 and y % 5 == 0:
        print "fizzbuzz" + "\n"
    elif y % 3 == 0:
        print "fizz" + "\n"
    elif y % 5 == 0:
        print "buzz" + "\n"
    else:
        print str(y) + "\n"
