# Write a program to for the below:
# a. The program should take inputs for Five Subjects. English, French, Mathematics, Physics, Chemistry
# b. Maximum Marks is 500 (100 Per Subject)
# c. Calculate the Percentage Scored

english = float(input("Enter marks for english (out of 100): "))
french = float(input("Enter marks for french (out of 100): "))
mathematics = float(input("Enter marks for mathematics (out of 100): "))
physics = float(input("Enter marks for physics (out of 100): "))
chemistry = float(input("Enter marks for chemistry (out of 100): "))

total_marks = english + french + mathematics + physics + chemistry
max_marks = 500
percentage = total_marks / max_marks * (100)
print(percentage)