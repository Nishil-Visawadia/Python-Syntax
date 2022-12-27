# comment the loop

# break - leaves the loop
# continue - leaves the iteration

for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i) 
  # above statement will not be printed for 10 as the pointer will move directly from continue (line 9) to for loop (line 6)


# emulate do-while loop
i = 0
while True:
  print(i)
  i = i + 1
  if(i%10 == 0):
    break
