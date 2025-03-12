'''(1.) To find the addition of two number.

a = 15
b = 10 
c = a + b
print(c)'''

#================================================================================================================
'''(2.) Print the "hello world"

print("Hello_Worlds")
'''
#==============================================================================================================
'''(3.) To find the square root of any integer.
#first solution :- we used "exponention arthmatical operator" to find the square root of any number.

a = 25
print(a**(1/2))

#second solution :- we used/import math library and used sqrt function which used to find out the square root.

import math
a = 25
print(math.sqrt(a))'''

#============================================================================================================
'''(4.) To calculate the Area of triangle.
base = 15
height = 10

area = 0.5*(base * height)
print(area)
'''
#============================================================================================================
'''(5.) Swap two number using third varible.
#first solution :-
a = 10
b = 15
temp = 0

temp = a
a = b 
b = temp
print(a,b)

#second soultion :-
a,b = b,a
print(a,b)'''

#================================================================================================================
'''#(6.) Swap two number without using third varible.
a = 10
b = 15

a = a + b
b = a - b
a = a - b
print(a,b)'''

#==========================================================================================================================
'''#(7.) Convert kilometers to miles.
km = float(input("Enter a kilometer :"))
miles = km * 0.621371
print(miles)'''

#==============================================================================================================================
'''#(8.) To check if number is  (+ve) and (-) number.
num = int(input('Enter any number :'))
if num > 0 :
    print("number is positive :",num)
elif num == 0 :
    print("Number is Zero :",num)    
else :    
    print("number is negative :",num)'''
    
#==================================================================================================================
'''#(9.) Check the number is Even or Odd.
num = int(input('Enter any number :'))   
if num % 2 == 0 :
    print("number is Even :",num)
else :
    print("Number is Odd :",num) '''

#===============================================================================================================
'''#(10.) To check the year is leap year.
year = int(input("Enter any year :"))
if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 )) :
    print("It is a leap year :",year)
else :
    print("It is not leap year :",year)'''
    
#=======================================================================================================================
'''#(11.) To find largest number among three numbers.
a = int(input("Enter a first number :"))    
b = int(input("Enter a first number :"))    
c = int(input("Enter a first number :"))    

if a > b and a > c :
    print("A is a largest :",a)
elif b > a and b > c :
    print("B is a largest :",b)
elif c > a and c > b :
    print("C is a largest :",c)
else :
    print("All three number are equal : ",a,b,c)'''
    
#===============================================================================================================
'''#(12.) To check the number is Prime or not.
num = int(input("Enter any number : "))
count = 0
for i in range (1,num+1):
    if num % i == 0 :
     count += 1
if count == 2 :
    print("It number is prime number : ",num)
else :
    print("It number is not prime number : ",num)'''
    
#==============================================================================================================
'''#(13.) Program to generate The Random number.
# we import the random library to get the randomely output and also we used the ''randint'' function for get random value/number
import random     

num = random.randint(0,10)
print(num)'''

#=======================================================================================================================
'''#(14.) Print prime number in a given range.
lowerRange = int(input("Enter lower limit here : "))
upperRange = int(input("Enter Upper limit here : "))

for num in range(lowerRange,upperRange+1) :
    if num > 1 :
      for i in range(2,num) :
        if num % i == 0 :
           break
      else :
            print(num,end=" ")
    else :
        print(num,end=" ")   
        '''
#=====================================================================================================================            
'''#(15.) To convert celsius to Fahrenhent
celsius = int(input("Enter temperture in celsius : "))

fahrenheit = (celsius *(9/5)) + 32
print(fahrenheit)                 
'''
#======================================================================================================================
'''#(16.) To find the factorial of a number.
num = int(input("Enter a any number : "))
fact = 1
for i in range(1,6) :
     if num % i == 0 :
         print(i)  '''       

#======================================================================================================================         
'''#(17.) To print a Table any given number.
num = int(input("Enter a any number : "))
for i in range(1,11) :
    print(num,"*",i,"=",i*num)'''
    
#=================================================================================================================
'''#(18.) To prinnt fibonacci series.0,1,1,2,3,5,8,13
num = 8
num1 = 0
print(num1)
num2 = 1
print(num2)
sum = num1 + num2
for i in range(0,8) :
    print(sum)
    num1 = num2
    num2 = sum 
    sum = num1 + num2 '''
    
#===========================================================================================================================
'''#(19.) To check armstrong numnber.
n = int(input("Enter a any number : "))
num = n
temp = 1
sum = 0
for i in range(1,n) :
    temp = n % 10
    print(temp)
    sum = sum + temp ** 3
    n = n // 10
    if n == 0 :
     break
if num == sum :
    print("It  is a armstrong number : ",sum)        
else :
    print("it is not amstrong number : ",num)  
      
'''
#==========================================================================================================================
'''#(20.) Find the sum of natural number.
num = 20
sum = 0
for i in range(1,5) :
    sum += i    
print(sum)   ''' 

#================================================================================================================================
#(21.) 


    
