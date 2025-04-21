# let Practice
# 1. WAP to input user's first name & print its length.

name = input("Enter your first name: ")
print(f"Length of your first name is: {len(name)}")

#2. WAP to find the occurrence of a 's' in a string

str = "hi, $my name is $ symbol $99.9"
print(f"Occurrence of '$' in the string is: {str.count('$')}")

# 3.WAP to check if a number entered by the user is odd or even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# 4. WAP to find the greatest of 3 numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the greatest number")
elif b >= c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")

# 5. WAP to check if a number is a multiple of 7 or not.

x = int(input('Enter a number: '))
if (x % 7 == 0):
    print(f"{x} is a multiple of 7")
else:
    print(f"{x} is not a multiple of 7")