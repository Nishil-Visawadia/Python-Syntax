marks = [3, 5, 6, "Test", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[11-3]) # Positive index
# print(marks[8]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# if 6 in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Te" in "Test":
#   print("Yes")

# print(marks)
# print(marks[:])
# print(marks[0:len(marks)])
# print(marks[1:])
# print(marks[1:-1]) # Negative index
# print(marks[1:10]) # Positive index
# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)