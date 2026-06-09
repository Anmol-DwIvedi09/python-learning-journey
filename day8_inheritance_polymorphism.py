# Inheritance

# class vehicle:
#     def start(self):
#         print ("Vehicle started")

# class car(vehicle):
#     pass

# my_car = car ()
# my_car.start ()

# Method Overiding

# class  Animal :
#     def speak(self):
#         print("Animal speaks")

# class cat(Animal):
#     def speak (self):
#         print("Meow")

# cat = cat()
# cat.speak()

# Polymorphism

# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# class Bird:
#     def sound(self):
#         print("Chirp ")

# animals = [Dog(), Cat(), Bird()]

# for animal in animals:
#     animal.sound()

# Encapsulation 

# class BankAccount :
#     def __init__(self, balance):
#         self.__balance = balance # private attribute

# # getter 
#     def get_balance(self):
#         return self.__balance
    
# #setter
#     def set_balance(self, balance):
#         self.__balance = balance
    
# account = BankAccount(10000)

# print("Balance :", account.get_balance())

# account.set_balance(20000)

# print("Updated Balance :", account.get_balance())

# Student Management

# class Student :
#     def __init__(self, name, roll_no):
#         self.name = name 
#         self.__roll_no = roll_no # private attribute 

# #getter 
#     def get_roll_no(self):
#         return self.__roll_no 

# #setter
#     def set_roll_no(self, roll_no):
#         self.__roll_no = roll_no

#     def display(self):
#         print("Name :", self.name)
#         print("Roll no :", self.__roll_no)

# student = Student("Anmol", 101)

# student.display()

# print("\n RollNo using getter :", student.get_roll_no())

# student.set_roll_no(102)

# print("Updated Rollno :", student.get_roll_no() )

# Mini Assignment 

# class Employee :
#     def __init__(self, name , salary):
#         self.name = name 
#         self.salary = salary

# class Manager(Employee) :
#     def __init__(self, name, salary, department):
#        super(). __init__(name, salary)
#        self. department = department

#     def display(self):
#         print("Name :", self.name)
#         print("Salary :", self.salary)
#         print("Department :", self.department)

# manager1 = Manager ("Anmol", 50000, "IT")
# manager2 = Manager ("Mohit", 60000, "Cs")

# manager1.display()
# manager2.display()


