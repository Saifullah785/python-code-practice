# 1.python Program to find the Factorial of a Number

# Solution ( Factorial : Using For Loop) 
# 5! = 5*4*3*2*1 = 120

# num = int(input("enter a number here: "))

# fact =1

# if num < 0 :
#     print ('factorial of 0 does not exist')
# if num ==0 :
#     print ('factorial of 0 ', 1)
# if num > 0:
#     for i in range (1, num+1):
#         fact = fact * i 
# print (' the factorial of the given number is', fact)

#Solution 2 (Using Recursion)

# def fact (a):
#     if a == 0:
#         return 1
#     else:
#         return ((a)*fact(a-1))
    
# num = int(input('enter a number here: '))

# result = fact(num)
# print ('the factorial of the given number is ',result)

#============================================================

# 2. Python Program to Display the multiplication table

# Solution 1 (Using for loop)

# n = int(input('enter a number here: '))

# for i in range (1,11):
#     print(n, "x", i, "=" ,n*i)

# 2. Solution 2 (Using while loop)

# n =7
# i=1

# while i<=10:
#     print(n, "x",i , "=",n*i)
#     i +=1

#============================================================

# 3. Python Program to print the fibonacci sequence

# Solution: (Fibonacci Sequence) 0,1,1,2,3,5,8

# a = 0
# b= 1
# num = int(input("enter a number to obtain fibanacci sequence: "))

# if num ==1:
#     print (a)
# else:
#     print (a)
#     print (b)
#     for i in range (2, num):
#         c = a + b
#         a = b
#         b = c
#         print (c)


#============================================================
# 4. Python Program to check Armstrong Number

#1. Solution (check Armstrong Number) # 0,1,153,370,371,407,1634

# num = int(input('enter a number here: '))


# sum = 0
# temp = num

# while temp> 0:
#     digit = temp%10
#     sum += digit ** 3
    
#     temp //= 10

# if sum == num :
#     print ('it is an armstrong number')
# else:
#     print ("it is not an amrstrong number")



#2. Solution 
# # Take input from user
# num = int(input("Enter a number to check if it's an Armstrong number: "))

# # Store the original number
# original_num = num

# # Initialize sum
# sum_of_powers = 0

# # Count the number of digits
# num_digits = len(str(num))

# # Calculate the sum of digits raised to the power of number of digits
# while num > 0:
#     digit = num % 10
#     sum_of_powers += digit ** num_digits
#     num //= 10

# # Check if original number equals the sum of powered digits
# if original_num == sum_of_powers:
#     print(f"{original_num} is an Armstrong number.")
# else:
#     print(f"{original_num} is NOT an Armstrong number.")


#============================================================

# 5. Python Program to find Armstrong Number in an Interval
# Solution (Armstrong Number in an Interval)

# lower = int(input('enter the lower limit here : '))
# upper  = int (input("enter the upper limit here: "))


# for num in range (lower, upper+1):
#     order = len(str(num))
#     sum = 0
#     temp =num 
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //=10
#     if num == sum:
#         print(num)
        
#============================================================


#Solution  (Sum of Natural Numbers)

# num = int(input("enter a number here: "))

# if num < 0 :
#     print ('print enter positive number ')
# else:
#     sum =0
#     while num>0:
#         sum +=num
#         num -=1
#     print (sum)

#============================================================

# 7. Python Program to Display Power of 2 Using Anonymous Function

# SOlution (Lambda Function)

# nterms = int(input('enter number of terms here: '))

# result = list(map(lambda x : 2 ** x, range(nterms+1)))

# # print (result)

# for i in range (nterms+1):
#     print ('the value of 2 raised to power',i, "is", result[i])


#============================================================

# 8. Python Program to Find Number Divisible by Another Number

##SOlution 1 (For Loop & Conditional statements)

# for i in range (1,100):

#     if i % 13 == 0:

#         print (i)

##Solution 2 (Using Lambda & filter() Function)

# l = [39,55,57,68,65,87]

# result = list(filter(lambda x : x % 13 == 0, l))

# print ('the number divisible by 13 are',result)

##============================================================

# 24. Python Program to Convert Decimal to Binary, Octal and Hexadecimal

## Solution (Binary, Octal And Hexadecimal)
# decimal = int(input('enter a number here: '))

# print ('the conversion of decimal number',decimal, "is: ")
 
# print (bin(decimal), 'in binary')

# print (oct(decimal), "in octal")

# print (hex(decimal), "in hexadecimal")

##============================================================

# 26. Python Program to Find HCF or GCD

## Solution (HCF\GCD)

# def findhcf(x,y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range (1, smaller+1):
#         if ((x %i ==0) and (y % i == 0)):
#             hcf = i
#     return hcf
# print ('the hcf of the given two number is ',findhcf(12,30))      


##============================================================

# 27. Python Program to Find the Factors of a numbers

# num = int(input('enter a number here: '))
 
# for i in range (1,num+1):
#     if num% i ==0:
#         print(i)

##============================================================

# 28. Python Program to Make a Simple Calculator(mini calculator)

# print ("============ MINI CALCULATOR ============")

# num1 = float(input('enter first number here: '))
# num2 = float(input("enter second number here: "))

# print(' press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division ')

# choice = int(input("enter your choice from 1 - 4: "))

# if choice == 1:
#     print (" The addition of given two numbers is" ,num1 + num2)
# elif choice == 2 :
#     print (" The subtraction of given two numbers is" ,num1 - num2)
# elif choice == 3 :
#     print (" The Multiplication of given two numbers is" ,num1 * num2)
# elif choice == 4 :
#     print (" The division of given two numbers is" ,num1 / num2)
# else:
#     print('invalid input')


 ##============================================================

# 30. Python Program to Display Calendar

# Solution (Display calendar)

# import calendar

# year = int(input('enter year: '))
# month = int(input('enter month: '))

# calendar = calendar.month(year, month)

# print (calendar)

 ##============================================================