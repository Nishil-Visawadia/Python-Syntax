def square(n):
    '''Takes in a number n, returns the square of n'''  # this is a doc string
    print(n**2)


square(5)
print(square.__doc__)  # this will print it



def square_1(n):
    print(n)
    '''Takes in a number n, returns the square of n'''  # this is a doc string
    print(n**2)


square_1(5)
print(square_1.__doc__)  # this will print "None" as there line between def and docstring


# write the following statement in terminal of python
# import this
