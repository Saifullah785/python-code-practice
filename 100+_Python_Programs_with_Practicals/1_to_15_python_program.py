# 2.Solution 2 (with user_inputs)

# num1 = float(input("Enter a number her: "))
# num2 = float(input("Enter another number here: "))

# sum = num1 + num2

# print ("the sum of the provided two number is", sum)

#===========================================================

#3.Python program to find the square root

#solution 1 (using exponentiation)

# num =64
# num1 = int(input('enter a number here:'))
# sr = num1**(1/2)
# print('the square root of the given number:',sr)

#solution 2 (using math module)
# import math

# num = int(input("enter a number here: "))
# sr = math.sqrt(num)
# print ("the root of the given number is : ",sr)

#===========================================================

# Python Program to calculate the Area of a triangle

# 1. solution (0.5 * base * height)

# height = float(input("enter the height of the triangle:"))
# base = float(input("enter the base of the triangle:"))

# area = (1/2)*base*height # or 0.5
# print ("the area of triangle is ",area)

#=============================================================

#5.Python Program to solve Quadratic Equation
# Solution 1
# Quadratic equation ===== ax**2 + bx + c = 0
# a, b and c are real numbers
# a! = 0
# import cmath

# a = int(input("enter number (a!=0): "))
# b = int(input("enter number: "))
# c = int(input("enter number: "))

# # formula for discriminant

# d = (b**2) - (4*a*c) 
# root1 = (-b-cmath.sqrt(d))/2*a
# root2 = (-b+cmath.sqrt(d))/(2*a)

# print ('the root are', root1, "and", root2)

#=============================================================

#8. Python Program to Convert Kilometers to Miles
# Solution - ===== Kilometers to miles ==== 1 kilometer = 0.621371 Mile

# km = float(input("enter your value in kms: "))

# miles = (0.621371)*km

# print (km, "kms in miles will be ", miles, "miles")

#=============================================================

#9. Python program to convert celsius To Fahrenheit
# solution (Celsius To Fahrenheit) / 0 celsius = 32 Fahrenheit
# (c*9/5)+32 = F

# celsius = int(input("enter temperature in celsius: "))

# fahrenheit = (celsius * (9/5))+32

# print ("the converted value is", fahrenheit, "Fahrenheit")

#=============================================================

# num = int(input('enter a number here: '))

# if num % 2 ==0:
#     print ('It is an even number: ')
# else:
#     print ('It is an odd number: ')

#=============================================================

# year = int(input('enter a year: '))
# if (year % 400==0) and (year % 100 == 0):

#     print (year, 'is a leap year')

# elif (year % 4 == 0) and (year % 100 != 0):

#     print(year, 'is a leap year')
# else:

#     print(year, 'is not a leap year' )

#=============================================================

#13. Python Program to find the largest among three numbers
# Solution  (Using Conditional Statements)

# num1 =int(input("enter the 1st number here:  "))

# num2 =int(input("enter the second number here:  "))
# num3 = int(input("enter the third number here:  "))

# if (num1 > num2) and (num1 > num3):
#     print (num1, "is a largest number")
# elif (num2 > num1) and ( num2 > num3):
#     print (num2, "is the largest number")
# else:
#     print (num3, "is the largest number")

#=============================================================


#14 Python program to check Prime Number 
# Solution (Prime Number)

# num = int(input("enter the number here: "))
# if num == 1:
#     print ("it is not a prime number")
# if num > 1 :
#     for i in range (2, num):
#         if num % i == 0:

#             print ('it is not a prime number')
#             break
#     else:
            
#         print("it is a prime number")

#=============================================================

#15. Python Program to print all prime Number in an Interval
# Solution (Prime Numbers in an Interval)

# lower = int(input("enter lower limit here: "))
# upper = int(input('enter upper limit here: '))

# for num in range (lower, upper+1):
#     if num>1:
#         for i in range (2,num):
#             if num%i ==0:
#                 break 
#         else:
#             print (num)

#=============================================================
