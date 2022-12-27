name = "Test"
friend = "User"
anotherFriend = 'tester'

print("Hello, " + name)

apple = "He said, \"I want to eat an apple\"" # First way
print(apple)
apple = 'He said, "I want to eat an apple"' # Second way
print(apple)

# Multiline
apple = '''He said,
Hello
Hi, I am good
"I want to eat an apple"'''
print(apple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4]) #Throws an error
print("\n")

print("Lets use a for loop\n")
for character in name:
    print(character)