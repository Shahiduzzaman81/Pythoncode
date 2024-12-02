# 6.Write a program to cheke prime number.
 
def check_p(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
            return True
 
mynum = int(input("enter a num : "))
check = check_p(mynum)
 
if check_p(mynum):
    print(f"{mynum} is a prime num ")
else:
    print(f"{mynum} is not a prime num ")
 
 
 
 
 
 
 
 
# 7.Write a program to Print Fibonacci series.
 
def fibo(x):
    first = 0
    second = 1
    print(f"{first} {second}",end=" ")
    for i in range(3,x+1):
        fibo = first+second
        first = second
        second = fibo
        print(fibo,end=" ")
 
 
n = int(input("Enter a range : "))
if n<=0:
    print("Please enter a positive integer")
else:
    print(f"Fibonacci series till {n}th ")
    fibo(n)
 
 
 
 
 
# 8.Write a program to calculate factorial.
 
def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact*=i
    return fact
 
n = int(input("Enter a positive number : "))
ans = factorial(n)
print(f"Factorial of {n} = {ans}")
 
 
 
 
 
 
# 9.Write a program to swap two number.
 
 
def mySwap(x,y):
    x,y = y,x
    return x,y
 
a = int(input("Enter the first number, A = "))
b = int(input("Enter the second number, B = "))
print(f"Before Swap A = {a} & B = {b}")
 
Result = mySwap(a,b)
 
print(f"After Swap = {Result}")
 
 
 
 
 
# 10.Write a program to cheke palindrome of number.
 
 
def is_palindrome(s):
 
    s = s.replace(" ", "").lower()
 
    return s == s[::-1]
 
 
Given = input("Enter a string = ")
 
if is_palindrome(Given):
    print(f"{Given} is a Palindrome")
 
else:
    print(f"{Given} is not a Palindrome")
 
 