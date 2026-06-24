# Modules & Packages 

# Use math module 

# import math 

# print(math.sqrt(81))
# print(math.factorial(6))

# random number 

# import random 

# for _ in range(5):
#    print(random.randint(1, 50))

# print currentdate and currenttime 

# from datetime import datetime

# now = datetime.now()

# print(now)

# List all files in your current directory using os

# import os 

# files = os.listdir()

# print("Files and folders in current dictionary")
# for file in files:
#     print(file)

# Convert dictionary to Json

# import json

# student = {
#     "name": "Anmol",
#     "age": "23",
#     "course": "CSE"
# }
  
# json_data = json.dumps(student)

# print(json_data)

# Read a CSV file and print all rows

# import os
# import csv

# current_folder = os.path.dirname(__file__)
# csv_path = os.path.join(current_folder, "students.csv")

# with open(csv_path, "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# Mini Assignment 

# import csv

# FILE_NAME = "students.csv"


# # Add Student
# def add_student():
#     try:
#         name = input("Enter Student Name: ")
#         age = int(input("Enter Student Age: "))

#         with open(FILE_NAME, "a", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow([name, age])

#         print("Student added successfully!\n")

#     except ValueError:
#         print("Age must be a number!\n")

#     except Exception as e:
#         print("Error:", e)


# # Read All Students
# def read_students():
#     try:
#         with open(FILE_NAME, "r") as file:
#             reader = csv.reader(file)

#             print("\n----- Student Records -----")

#             for row in reader:
#                 print(row)

#             print()

#     except FileNotFoundError:
#         print("No student records found.\n")

#     except Exception as e:
#         print("Error:", e)


# # Main Menu
# def main():
#     while True:
#         print("===== Student CSV Manager =====")
#         print("1. Add Student")
#         print("2. View Students")
#         print("3. Exit")

#         choice = input("Enter Choice: ")

#         if choice == "1":
#             add_student()

#         elif choice == "2":
#             read_students()

#         elif choice == "3":
#             print("Program Closed.")
#             break

#         else:
#             print("Invalid Choice!\n")


# main()
