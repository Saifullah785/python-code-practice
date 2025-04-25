
## 31. Python Program to Display Fibonacci Sequence Using Recursion
## Solution: (Display Fibonacci Sequence)


def fibo (n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input("enter a number here: "))

if n <=0:
    print('enter a positive number')
else:
    print ('Fibonacci Sequence')
    for i in range (n):
        print (fibo(i))



##==========================================================

## 32 Python Program to Find Sum Of Natural Numbers Using Recursion

##Solution 1 (Harry,Potter And The Goblet of fire)

def NNS (n):
    if n <= 1:
        return n 
    else:
        return (n)+NNS(n-1)

n = int(input("enter a number here"))
if n<=0:
    print ('enter a positive number: ')
else:
    print ('The sum of natural number upto given number is:',NNS(n))


##==========================================================

## 33. Python Program to Find Factorial of Number Using Recursion

## Solution (Factorial)
def fact (n):
    if n == 1:

        return 1
    else:
        return (n*fact(n-1))
    
n = int(input('enter a number here: '))
if n <=0:
    print ('Factorial of number less than 1 does not exists')

else:
    print ('Factorial of given number is', fact(n))

##==========================================================

## Solution (Decimal to Binary Using Recursion)

def ConvertBinary(n):
    if n >1:
        ConvertBinary(n//2)
    print (n%2, end = "")

print ("the binary of the given number is: ")

ConvertBinary(10)

##==========================================================

## Solution (Matrix Addition)

A =[[1,5,8],
    [4,6,7],
    [7,2,3]]
B= [[4,5,6],
    [8,9,1],
    [3,5,6]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(r)

##==========================================================

## 36. Python Program to Transpose a Matrix
##Solution 1 (Using For Loop)

A = [[1,2,3],
     [4,5,6]]
T = [[0,0],
     [0,0],
     [0,0]]
for i in range (len(A)):
    for j in range (len(A[0])):

        T[j][i] =A[i][j]
for i in T:
    print(i)

##Solution 2 (Using list comprehension)

A = [[1,2,3],
     [4,5,6]]

T = [[A[j][i] for j in range (len(A))] for i in range  (len(A[0]))]

for i in  T:
    print (i)

##==========================================================
## 37. Python Program to Multiply Two Matrices
## Solution (Matrix Multiplication)

A= [[1,2,3],
    [4,5,6],
    [7,8,9]]
B= [[1,2,1,1],
    [4,2,1,2],
    [6,3,4,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
for i in range (len(A)):
    for j in range (len(B[0])):
        for k in range (len(B)):
            result[i][j] += A[i][k] * B[k][j]

for i in result:
    print (i)


##==========================================================

# 38. Python Program to Check Whether a String is Palindrome or Not

## Solution (Palindrome)

a = input('Enter a word her: ')

rev = a[: : -1]

if a == rev:
    print ('it is palindrome')
else:
    print ('it is not palindrome')

##==========================================================

# 39.Python Program to Remove Punctuations From a String

## Solution (Using For Loop) punctuations (){}-_, ""=!<>
punc ='''!@#$%^&*()_{}[]|":/<>~'''
string = input('enter anything here: ')

empty_str =''
for i in string:
    if i not in punc:
        empty_str = empty_str + i

print(empty_str)

##==========================================================

## Solution 1 (Using String Funcctions ANd for Loop)

a = input('enter something here: ')
w = a.split()
print (w)
for i in range (len(w)):
    w[i] = w[i].lower()

#print (w)
w.sort()
print (w)

for i in w:
    print (i)

##==========================================================

## Solution 1 (Using Dictionary)
a = "Harry Potter and the Prisoner of Azkaban"
vowels = "aeiou"
a = a.casefold()
print (a)
count = {}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char]+=1

print (count)

##==========================================================
# 44. python Program to Merge Two Dictionaries

## Solution 1 (Using / Operator)
dic1 = {"John":89, "Lisa": 99}
dic2 = {"Lisa":94, "Peter":78}

print (dic1 | dic2)

##==========================================================