i = 0
while i<7:
  print(i)
  i = i + 1
#   if i == 4:
#     break

else:
  print("Sorry no i\n")


for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("sorry no i \n")


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


# Important Interview Question:

# How can we use "else" in the for loop ?
# Yes

# If "Loop" has been broken (break) , now tell will the content of 'else' be printed ?
# No, 'else' will not be printed as the loop has successfully executed till break statement
