# database = [
#     ["What is Google", "Web browser", "Mouse", "Keyboard", "Monitor"],
#     ["Who invented Python Language", "George Bush", "You", "Guido van Rossum", "Elon Musk"],
#     ["What is Python used for", "Data Visualization", "Data Analytics", "Web Applications", "All of the above"],
#     ["How many Colors are there in Rainbow", 10, 7, 9, 2],
#     ["Who are you", "Water Bottle", "Human", "Keyboard", "Walmart Bag"]
# ]

# wallet = 0

# print("---------- There are 5 questions in this quiz ----------")

# for i in range(len(database)):
#     if i == 0:
#         print("\n""Q:", database[0][0] + "\n" + "A:", database[0][1] + "\n" + "B:", database[0][2] + "\n" + "C:", database[0][3] + "\n" + "D:", database[0][4] + "\n" + "This question is worth ₹ 1000")
#         ans = str(input("Enter the option: ")).upper()
#         print(ans)
#         if ans == "A":
#             wallet += 1000
#             print("Correct answer. You have won ₹", wallet)
#         else:
#             print("Wrong answer, \"A\" was the correct option. You go home with ₹", wallet)
#             break
#     if i == 1:
#         print("\n""Q:", database[1][0] + "\n" + "A:", database[1][1] + "\n" + "B:", database[1][2] + "\n" + "C:", database[1][3] + "\n" + "D:", database[1][4] + "\n" + "This question is worth ₹ 5000")
#         ans = str(input("Enter the option: ")).upper()
#         print(ans)
#         if ans == "C":
#             wallet += 5000
#             print("Correct answer. You have won ₹", wallet)
#         else:
#             print("Wrong answer, \"C\" was the correct option. You go home with ₹", wallet)
#             print("Congratulations on reaching this far in the quiz")
#             break
#     if i == 2:
#         print("\n""Q:", database[2][0] + "\n" + "A:", database[2][1] + "\n" + "B:", database[2][2] + "\n" + "C:", database[2][3] + "\n" + "D:", database[2][4] + "\n" + "This question is worth ₹ 10000")
#         ans = str(input("Enter the option: ")).upper()
#         print(ans)
#         if ans == "D":
#             wallet += 10000
#             print("Correct answer. You have won ₹", wallet)
#         else:
#             print("Wrong answer, \"D\" was the correct option. You go home with ₹", wallet)
#             print("Congratulations on reaching this far in the quiz")
#             break
#     if i == 3:
#         print("\n""Q:", database[3][0] + "\n" + "A:", str(database[3][1]) + "\n" + "B:", str(database[3][2]) + "\n" + "C:", str(database[3][3]) + "\n" + "D:", str(database[3][4]) + "\n" + "This question is worth ₹ 15000")
#         ans = str(input("Enter the option: ")).upper()
#         print(ans)
#         if ans == "B":
#             wallet += 15000
#             print("Correct answer. You have won ₹", wallet)
#         else:
#             print("Wrong answer, \"B\" was the correct option. You go home with ₹", wallet)
#             print("Congratulations on reaching this far in the quiz")
#             break
#     if i == 4:
#         print("\n""Q:", database[4][0] + "\n" + "A:", database[4][1] + "\n" + "B:", database[4][2] + "\n" + "C:", database[4][3] + "\n" + "D:", database[4][4] + "\n" + "This question is worth ₹ 50000")
#         ans = str(input("Enter the option: ")).upper()
#         print(ans)
#         if ans == "B":
#             wallet += 50000
#             print("Correct answer. You have won ₹", wallet)
#             print("You have WON the quiz !!!\n")
#         else:
#             print("Wrong answer, \"B\" was the correct option. You go home with ₹", wallet)
#             print("Congratulations on reaching this far in the quiz")
#             break
