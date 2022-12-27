a = 1 # this is int
print(a)

b = True # this is boolean
print(b)

c = "Test" # this is string
print(c)

d = None # a none type variable
print(d)

print("type of variable", type(a))
print("type of variable", type(b))
print("type of variable", type(c))
print("type of variable", type(d))

e = complex(2, 2)
print(e)

# Collection of different data types and can also be changed (mutable)
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

# cannot be modified (immutable)
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# dictionary is a collection of key-value pairs
dict1 = {"name":"ABC", "age":20, "canVote":True} # name is key and ABC is value
print(dict1)

# Everything in Python is an Object