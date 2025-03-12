'''Q.1 Write a program accepts two numbers from user and calculates first no is divisible by second or
not.
num1 = int(input("Enter a first number = "))
num2 = int(input("Enter a second number = "))
if (num1 % num2 == 0) :
    print("first number is divisible by second number")
else :
    print("first number is not divisible by second number")    


# Q.2 Write a program accepts a number from user and check given number is even or odd.
n = int(input("Enter a any  number = "))
if n % 2 == 0 :
    print("number is even number = ",n)
else :
    print("number is a odd number = ",n)     


# Q.3 Write a program accepts a number from user and check given number is palindrome number or
#not.
n = int(input("Enter a any three digit number = "))
num = n
temp = 0
revNum = 0
temp = n % 10
revNum = revNum * 10 + temp
n = n // 10

temp = n % 10
revNum = revNum * 10 + temp
n = n // 10

temp = n % 10
revNum = revNum * 10 + temp
n = n // 10

if revNum == num :
    print("number is a palindrone number = ",num)
else :
    print("number is not a palindrone number = ",num)    


# Q.4 Write a program accepts a number from user and check given number is Armstrong number or not.
n = int(input("Enter a any three digit number = "))
num = n
temp = 0
sum = 0
temp = n % 10 
sum = sum + temp ** 3
n = n // 10

temp = n % 10 
sum = sum + temp ** 3
n = n // 10

temp = n % 10 
sum = sum + temp ** 3
n = n // 10

if num == sum :
    print("number is Armstrong number = ",num)
else :
    print("number is not Armstrong number = ",num)   



# Q.5 Write a program accept a three digits number from user and check biggest digit of given number.
num1 = int(input("Enter a first number = "))
num2 = int(input("Enter a second number = "))
num3 = int(input("Enter a third number = "))
if num1 > num2 and num1 > num3 :
    print("first number is greater = ",num1)
elif num2 > num1 and num2 > num3 :
    print("second number is larger = ",num2)
elif num3 > num1 and num3 > num2 :
    print("third number is larger = ",num3)
else :
    print("both number are equal")        
    
    
# Q.6 Write a program that accepts the age of person, find out the person is eligible for voting or not.
age = int(input("Enter your age = "))
if age >= 18 :
    print("your are eligible for voting ")
else :
    print("you are not eligible for voting")    
    

# Q.7 Write a program that accepts a number from user and calculate whether it is positive or negative
# or zero
n = int(input("Enter a any number = "))
if n > 0 :
    print("positive number = ",n)
elif n < 0 :
    print("number is negative =") 
else :
    print("number is Zero = ",n)       


# Q.8 Write a program to calculate whether character is in lowercase or uppercase.
ch = input("Enter your single character = ")
if ch >= 'A' and ch <= 'Z' :
    print("character is a uppercase = ",ch)
else :
    print("charater is lower case = ",ch)   


# Q.9 Write a program to calculate whether year is leap year or not.
n = int(input("Enter a year = "))
if (n % 4  == 0 and n % 100 != 0) or n % 400 == 0 :
    print("this is a leap year = ",n)
else :
    print("this is not leap year = ",n)  
    
    
#Q.10 Write a program to calculate whether a character is vowel or consonant.
ch = input("Enter a any single character = ")
if (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U') or (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u') :
    print("character is vowels = ",ch)
else :
    print("character is consonent = ",ch)   
    
    
Q.11 Write a program that accepts five subjects’ marks from user and calculate the total marks then
calculate
Percentage Display message according to following condition.
Percentage >=60 then print message Grade A
Percentage >=50 then print message Grade B
Percentage >= 40 then print message Grade C
Percentage < 40 then print message Grade D
m = int(input("Enter maths marks = "))
p = int(input("Enter physics marks = "))
c = int(input("Enter chemistry marks = "))
h = int(input("Enter hindi marks = "))
e = int(input("Enter english marks = "))
totalMarks = m + p + c + h + e
print("total marks = ",totalMarks)
per = (totalMarks * 100 ) / 500
print("percentage is = ",per)

if per >= 60 :
    print("GRADE A ")
elif per >= 50 :
    print("GRADE B ")
elif per >= 40 :
    print("GRADE C ")
else :
    print("GRADE D ") 


#Q.12 Write a program for generating electricity Bill Accept last month unit and current month unit from
user, then calculate and print bill amount according to following condition
0-150 charges 4 rs/unit
151-300 charges 6 rs/unit
301-500 8rs/unit
>500 charges 10rs/unit
currMonth = float(input("Enter a current month bill = "))
lastMonth = float(input("Enter a last month bill = "))
bill = currMonth - lastMonth
if bill >= 0 and bill <= 150 :
    print("Bill is = ",(bill*4))
elif bill >= 151 and bill <= 300 :
    print("Bill is = ",(bill*6))
elif bill >= 301 and bill <= 500 :
    print("Bill is = ",(bill*8))
else : 
    print("Bill is = ",(bill*10))            


Q.13 Write a program to accept basic salary from user, if basic salary is between 0 and 15000 then TA is
8% of basic salary, DA is 4% of basic salary. If salary is above 15000 then TA is 10% of basic salary, DA is
5% of basic. Calculate gross salary as gs=basic salary+TA+DA?
basicSalary = float(input("Enter your basic salary = "))
if basicSalary >= 0 and basicSalary <= 15000 :
    ta = (basicSalary * 8) // 100
    print("T.A. = ",ta)
    da = (basicSalary * 4) // 100
    print("D.A. = ",da)
    gs = basicSalary + ta + da
    print("G.S. = ",gs)
    
else :
    ta = (basicSalary * 10) // 100
    print("T.A. = ",ta)
    da = (basicSalary * 5) // 100
    print("D.A. = ",da)
    gs = basicSalary + ta + da
    print("G.S. = ",gs)
    
    
# Q.14 write a program to create area caculator__
print("*****AREA CALCULATOR*****")    
print("""Press 1 to get the area of square :
      Press 2 to get the area of rectangle :
      Press 3 to get the area of circle :
      Press 4 to get the area of triangle :""")
choice = int(input("Enter a number between 1-4 : "))
if choice == 1 :
    side = float(input("Enter one side of square : "))
    area = side * side
    print("Area of square is : ",area)
elif choice == 2 :    
    length = float(input("Enter length of rectangle : "))
    breadth = float(input("Enter breadth of rectangle : "))
    area = length * breadth
    print("Area of rectangle is : ",area)
elif choice == 3 :
    radius = float(input("Enter a radius of circle : "))
    area = 3.14 * radius**2
    print("Area of circle is : ",area)
elif choice == 4 :
    base = float(input("Enter base of triangle : "))
    height = float(input("Enter height of triangle : "))
    area = 0.5 * base * height
    print("Area of triangle is : ",area)   
else :
    print("Enter invalid number")    
    
        
#Q.15 write a program check whether the passed letter is vowels or not___
letter = input("Enter a letter here : ")
if (letter in "aeiou") or (letter in "AEIOU")  :
    print("it is vowels")
else :
    print("it is not vowels")  
    
    
#Q.16 writ a program to check if a number is a single digit number , 2-digit number and so on ----,upto 5 digits
num = int(input("Enter upto 5 digits number only : "))
if num >= 0 and num <= 9 :
    print("single digit number")
elif num >= 10 and num <= 99 :
    print("two digit number")
elif num >= 100 and num <= 999 :
    print("three digit number")
elif num >= 1000 and num <= 9999 :
    print("four digit number")
else :
    print("five digit number ")   
                 
    
#Q.16 Create a calculator_____
print("*****CACULATOR*****")
print("""Press + operation to calculate sum of two number
      Press - operation to calculate subtract of two number
      Press * operation to calculate product of two number
      Press // operation to calculate divide of two number
      Press % operation to calculate remainder of two number""") 
choice = input("Enter a given symbol option : ")
if choice == '+' :
    a = int(input("Enter first value = ")) 
    b = int(input("Enter second value = "))      
    print("sum is = ",(a+b))
elif choice == '-' :
    a = int(input("Enter first value = ")) 
    b = int(input("Enter second value = "))      
    print("subtraction is = ",(a-b))
elif choice == '*' :
    a = int(input("Enter first value = ")) 
    b = int(input("Enter second value = "))      
    print("product is = ",(a*b))
elif choice == '//' :
    a = int(input("Enter first value = ")) 
    b = int(input("Enter second value = "))      
    print("dividend is = ",(a//b))
elif choice == '%' :
    a = int(input("Enter first value = ")) 
    b = int(input("Enter second value = "))      
    print("remainder is = ",(a%b))         
else :
    print("enter invaild symbol")           '''