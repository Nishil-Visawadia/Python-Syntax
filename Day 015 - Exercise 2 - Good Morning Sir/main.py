import time

timestamp = time.strftime('%H:%M:%S')
print(type(timestamp))
print("Time is ", timestamp)

hour = int(time.strftime('%H'))
print(type(hour))
print("Hour is :", hour)

# if - elif - else loop
if (hour >= 0 and hour < 6):
    print("Good Night Sir !")
elif (hour >= 6 and hour < 12):
    print("Good Morning Sir !")
elif (hour >= 12 and hour < 18):
    print("Good Afternoon Sir !")
elif (hour >= 18 and hour < 24):
    print("Good Evening Sir !")
else:
    print("Invalid Syntax")
