# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)
# average(2, 4)
# average(4, 6)
# average(b=9)


# (* & **) is used for multiple arguments
def average(*numbers):
    print(type(numbers)) # used as tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum / len(numbers))
    # return 7
    return sum / len(numbers)


c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name)) # used as dictionary (key:value)
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
