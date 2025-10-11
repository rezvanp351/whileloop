# ==============================================
# Python While Loops, Break, Continue, If/Elif/Else
# ==============================================
# Author: Rezvan Panah
# Description:
# This tutorial explains Python "while loops" and control statements (break, continue, if/elif/else)
# with clear examples and inline comments.
# Perfect for GitHub learning repositories or beginners who want to understand loop logic.

# ----------------------------------------------
# 🎯 Part 1: What is a while loop?
# ----------------------------------------------
# A while loop keeps running as long as the condition is True.

count = 1
while count <= 5:
    print("Count:", count)  # prints the current number
    count += 1              # increases the counter to avoid infinite loop

# ----------------------------------------------
# 🎯 Part 2: Using 'break'
# ----------------------------------------------
# 'break' immediately stops the loop even if the condition is still True.

# x = 1
# while x <= 10:
#     print("Number:", x)
#     if x == 5:
#         print("Breaking the loop at 5")
#         break   # stops the loop when x equals 5
#     x += 1

# ----------------------------------------------
# 🎯 Part 3: Using 'continue'
# ----------------------------------------------
# 'continue' skips the rest of the loop for the current iteration
# and moves to the next one.

# y = 0
# while y < 7:
#     y += 1
#     if y == 3:
#         print("Skipping number 3")
#         continue   # skip the rest of the code for y == 3
#     print("y =", y)
# ----------------------------------------------
# 🎯 Part 4: Combining while with if / elif / else
# ----------------------------------------------
# You can use conditional statements inside loops
# to perform different actions based on conditions.

# num = 1
# while num <= 7:
#     if num == 1:
#         print("One - Start of Loop")
#     elif num == 4:
#         print("Four - Middle of Loop")
#     elif num == 7:
#         print("Seven - End of Loop")
#     else:
#         print("Number:", num)
#     num += 1


# ----------------------------------------------
# 🎯 Part 5: Practical Example — User Input
# ----------------------------------------------
# This program keeps asking the user to enter a number until
# they type a negative number to exit.

# while True:
#     user_input = int(input("Enter a positive number (negative to exit): "))
#     if user_input < 0:
#         print("You entered a negative number. Exiting...")
#         break   # stop the loop
#     elif user_input == 0:
#         print("Zero entered, try again.")
#         continue   # skip this iteration
#     else:
#         print("You entered:", user_input)

# print("Program ended successfully!")
