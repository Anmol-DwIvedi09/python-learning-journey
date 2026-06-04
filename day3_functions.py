
area of circle function

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

r = float(input("enter the radius :"))

result = area_of_circle(r)

print ("area of circle  =", result)

Function to check Prime number

def is_prime(num):
    
    if num <= 1:
       return False

    for i in range(2,num):
        if num % i == 0:
           return False 
    
    return True  

number = int(input("Enter a number "))

if is_prime:
    print("Prime number")
else:
    print("Not a Prime number")

Function to reverse a number 

def reverse_number(num):

    reverse = 0

    while num > 0:
          digit = num % 10 
          reverse = reverse * 10 + digit
          num = num // 10
          
    return reverse 
    
number = int(input("Enter a number :"))

result = reverse_number(number)

print ("Reversed number =", result)

Function to count digits

def  count_number(num):

    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

number = int (input("Enter a number :"))

result = count_number(number)

print ("Number of digits :", result)

 Function to calculate average

def calculate_average(marks1 , marks2, marks3):
    
    Total = marks1 + marks2 + marks3 
    average = Total / 3

    return average 

m1 = float(input("Enter marks of sub1 :"))
m2 = float(input("Enter marks of sub2 :"))
m3 = float(input("Enter marks of sub3 :"))

result = calculate_average(m1, m2, m3)

print ("average is :", result)

Function to print multiplication table

def multiplication_table(num):

    for i in range(1, 11):
     print( num, "x", i, "=", num*i)

number = int(input("Enter a number :"))

multiplication_table(number)
