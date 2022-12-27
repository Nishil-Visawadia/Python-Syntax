name = 'Abhishek'
for i in name:
    print(i)
    if(i =="b"):
        print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k)

for k in range(5):
    print(k + 1)
  
for k in range(1, 5):
    print(k)

# start -> 1 , end -> 12 , step -> 3
# so it will print 1 skip (start)1 , 2 , 3 and print 4
for k in range(1, 12, 3):
    print(k)

# Reference: https://www.geeksforgeeks.org/python-range-function/