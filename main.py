print("Welcome To Python Debugging Session.")

# Desribe The Problem.
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You Got It...")
# my_function()

# Reproduce The Bug.
# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer.
# year = int(input("Enter Your Year Of Birth Here:\n"))
# if year > 1980 and year < 1994:
#     print("You Are A Millenial.")
# elif year > 1994:
#     print("You Are A Gen Z.")

# Fix The Errors.
# age = int(input("Enter Your Age Here:\n"))
# if age > 18:
#     print(f"You Can Drive At The Age : {age}.")

# Print Your Friens.
# pages = 0
# word_per_page = 0
# pages = int(input("Number Of Pages:\n"))
# word_per_page = int(input("Number Of Words Per Pages:\n"))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words)

# Use A Debugger.
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

# Debugging Odd Or Even.

# number = int(input("Enter The Number To Be Checked :\n"))

# if number % 2 == 0:
#     print("This Is An Even Number...")
# else:
#     print("This Is An Odd Number...")

# Debugging Leap Year.

# year = int(input("Enter Year To Be Checked:\n"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap Year...")
#         else:
#             print("Not A Leap Year...")
#     else:
#         print("Leap Year...")
# else:
#     print("Not Leap Year...")

# Debugging FIZZ BUZZ

# for number in range(1, 101):
#     print(f"Currently On Number: {number}.")
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)