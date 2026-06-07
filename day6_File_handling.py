# File handling And Exception handling

#Create a file and write your name

# with open ("myname.txt", "w") as file :
#     file.write("Anmol")
    
# print("File created and name written successfully!")

# Read content from a file

# with open ("myname.txt", "r") as file :
#      content=file.read()

# print(content)     

# Append a new line to a file

# with open("myname.txt", "a") as file :
#      file.write("\n Hello, this is new line. ")

# print("Line added successfully!")

# Count number of lines in a file

# with open("myname.txt", "r") as file :
#     lines = file.readlines()

# print("number of lines :", len(lines))

# Count number of words in a file
# with open ("myname.txt", "r") as file:
#     content = file.read()

# words = content.split()
# print("Total words are :", len(words))

# Exception handling 

# Handle division by zero

# try:
#     num1 = int(input("enter numerator: "))
#     num2 = int(input("enter denominator: "))

#     result = num1/num2
#     print("result is :", result)

# except ZeroDivisionError :
#      print("Error : cannot divide by zero!")

# Handle invalid integer input

# try: 
#     num = int(input("Enter a number: "))
#     print("You entered :", num)

# except ValueError :
#     print("Invalid input")

# Use try-except-else

# try:
#     num = int(input("Enter a number :"))

# except ValueError :
#     print("Invalid input")

# else :
#     print("Valid input")

# Use try-except-finally

# try: 
#     num1 = int(input("Enter a num 1 :"))
#     num2 = int(input("Enter a num 2 :"))

#     result = num1/num2
#     print("Result is :", result)

# except ZeroDivisionError :
#     print("Error : cannot be divide by zero")

# except ValueError :
#     print("Invalid input ")

# finally :
#     print("program executed completely")

# Raise a custom exception if age < 18

# try :
#     age = int(input("Enter your age :"))

#     if age < 18 :
#         raise Exception ("You must be over 18 years old.")
    
#     print("Access granted")

# except Exception as e :
#     print("Error :", e)

# Mini Assignment

# try : 
#     name = input("Enter student name :")

#     with open("students.txt", "a") as file :
#         file.write(name + "\n")

#     print("Student record saved successfully!")

#     print("\nAll Student Records:")
#     with open("students.txt", "r") as file:
#         records = file.read()
#         print(records)

# except FileNotFoundError:
#     print("Error: File not found!")

# except PermissionError:
#     print("Error: Permission denied!")

# except Exception as e:
#     print("An error occurred:", e)

# finally:
#     print("Program completed.")