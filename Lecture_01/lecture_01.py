

# Taking input from user & printing it


name = input("name: ")
age = int(input("enter the age: "))
price= float(input("enter the price: "))

print("hello ",name)
print("your age is ",age)
print("your price is ",price)

# Practice Time


# print output for :
# A = 10 & G = M
# A = 2 & G = F

A = int (input("A : "))
G = input ("M/F : ")
if ((A == 1 or A ==2) and G == "M"):
    print ("fee is 100")
elif ((A == 3 or A ==4) and G == "F"):
    print ("fee is 200")
elif (A == 5 and G == "M"):
    print ("fee is 300")  
else:
    print('no fee')

    # clever if / Ternary operator

# no.1
age = int (input("Enter your age: "))
vote = ("No", "yes") [age >= 18]
print(vote)

# no.2
sal = float(input('salary:'))
tax = sal*(0.1, 0.2)[sal >= 50000]
print (tax)

# input function program

name = input('Enter your name: ')
age = int(input('Enter your age:'))
marks = float(input('Enter your marks:'))

print('welcome:', name)
print('Age:', age)
print('Marks:', marks)

# program no 1

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
sum = first + second
print("Sum of two numbers is: ", sum)

#program no 2

side = float(input("Enter the side of square: "))
print("Area of square is: ", side * side)

# program no 3
a = float(input('enter first number: '))
b = float(input('enter second number: '))
print("avg =", (a + b) / 2)

#program no 4
a = int(input('enter the first number: '))
b = int(input('enter the second number:'))
 
print(a >=b)



