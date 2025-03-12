'''# Q.1 Write a program to print n natural number.
n =  int(input("Enter a number : "))
for i in range(1,n+1) :
    print(i)
   

# Q.2 Write a program to calculate factorial of given number.
n = int(input("Enter a number which number factorial you want : "))
fact = 1
for i in range(1,n+1) :
    fact *= i
print(fact)      


#Q.3 Write a program to calculate square from 1-10 numbers.
square = 0
for i in range(1,11) :
    square = i ** 2
    print(i,"square is = ",square) 


# Q.4 Write a program to print table of any given numbers.
n = int(input("Enter a number which table you want : "))
for i in range(1,11) :
    print(n,"*",i,"=",n*i) 
    

#Q.5 Write a program to find out reverse of a given number.
n = int(input("Enter a number : "))
temp = 1
revNum = 0
for i in range(1,n) :
    temp = n % 10
    revNum = revNum * 10 + temp
    n = n // 10 
    if n == 0 :
        break
print(revNum)   


# Q.6 Write a program that accepts a number from user and check given number is palindrome number
#or not.
n = int(input("Enter a number : "))
num = n
temp = 1
revNum = 0
for i in range(1,n) :
    temp = n % 10
    revNum = revNum * 10 + temp
    n = n // 10 
    if n == 0 :
        break
if num == revNum :
    print("it is a palindrone number : ",num)
else :
    print("It is not a palindrone number = ",num)   ''' 


#Q.7 Write a program that accepts a number from user and check given number is Armstrong number or
#not.
n = int(input("Enter a three digit number : "))
num = n
temp = 1
sum = 0
for i in range(1,n) :
    temp = n % 10
    sum = sum + temp ** 3
    n = n // 10 
    if n == 0 :
        break
if num == sum :
    print("it is a Armstrong number : ",num)
else :
    print("It is not a Armstrong number = ",num)   


'''# Q.8 Write a program that accepts a number from user calculate factor of a given number.
n = int(input("Enter a number : "))
for i in range(1,n) :
    if n % i == 0 :
        print(i) 


#Q.9 Write a program that accepts a number from user check given number is perfect number or not.
n = int(input("Enter a number : "))
num = n
sum = 0
for i in range(1,n) :
     if n % i == 0 :
            sum += i
if sum == num :
    print("It is a perfect number = ",num)            
else :
    print("It is not a perfect number : ",num)    
 

#Q.10 Write a program to print Fibonacci Series.
#0 1 1 2 3 5 8 13
#---------
n = int(input("Enter a number : "))
num1 = 0
num2 = 1
sum = num1 + num2
for _ in range(n) :
    print(num1,end=" ")
    num1 = num2
    num2 = sum
    sum = num1 + num2  


#Q.11 Write a program to calculate sum of digits of a number.
n = int(input("Enter a number = "))
sum = 0
temp = 0
for i in range(1,n) :
    temp = n % 10
    sum += temp 
    n = n // 10
    if n == 0 :
        break
print(sum)


#Q.12 Write a program to calculate sum of squares of n natural number.
n = int(input("Enter a number :"))
sum = 0
for i in range(1,n) :
    square = i ** 2
    sum += square
print("Sum is = ",sum)


#Q.13 Write a program to accept n number from user and show how many number are even or odd.
n = int(input("Enter a number : "))
count = 0
temp = 0
for i in range(1,n) :
    if i % 2 == 0 :
        count += 1
        print()
    else :
        temp += 1
print("Even number = ",count)
print("Odd number = ",temp)      

#Q.14 Write a program to find LCM of two numbers.
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
lcm = 0
hcf = 0
if num1 > num2 :
    big = num1
else :
    big = num2     
for i in range(2,big+1)  :
    if num1 % i == 0 and num2 % i == 0 :
        print("=======")
        hcf += i
lcm = (num1*num2) / hcf           
print("LCM is = ",lcm)
        

#Q.15 Write a program to find HCF of two numbers.
num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
lcm = 0
hcf = 0
if num1 > num2 :
    big = num1
else :
    big = num2     
for i in range(2,big+1)  :
    if num1 % i == 0 and num2 % i == 0 :
        print("HCF is = ",i)


#Q.16 Write a program that accepts a number from user and check given number is prime
n = int(input("Enter a number = "))
count = 0
for i  in range(1,n+1) :
    if n %  i == 0  :
      count += 1
if count == 2  :
    print("this number is prime : ",n)
else :
    print("this is number is not a prime number : ",n)        
    
    
#Q.17 write a program to check if a number is divisible by 8 and 12 to 100 numbers___
count = 0
temp = 0
for i in range(1,101) :
    if i % 8 == 0 and i % 12 == 0:
        print("divisible by 8 and 10 = ",i)  
 '''