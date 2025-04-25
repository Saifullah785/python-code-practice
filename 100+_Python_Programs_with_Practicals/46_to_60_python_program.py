## 51. Python Program to Catch Multiple Exceptions in One Line

## Solution 1 (Handling Multiple exceptions)

string = input('enter something here: ')

try:
    num = int(input('enter a number here: '))
    print (string + num)
except (ValueError, TypeError) as a:
    print (a)
print ('thank you')

##=========================================================

# 54. Python Program to check if a key is Already Present in a Dictionary

## Solution : (Check if A list is EMPTY)


friends = {"Rachel":"Ross","Monica": "chandler","Phoebe":"Joe"}

name = input('enter a key here: ')

if name in friends.keys():
    print ('it is present')

##=========================================================