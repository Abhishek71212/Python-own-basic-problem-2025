'''# Q.1 Write a program to find out square of given number.
n = int(input("Enter any number = "))
square = n * n
print("ypur square is = ",square)

# Q.2 Write a program to find out area of circle.
r = float(input("Enter a radius of circle = "))
Area = 3.14 * r * r
print("Area of circl  is = ",Area) 

# Q.3 Write a program to find out simple interest (SI).
p = 5000
r = 5
t = 3
si = (p * r * t) / 100
print("simple intrest is = ",si) 

# Q.4 Write a program accept 5 subject marks (Hint P=67,C=87,M=90,H=98,E=88) and calculate total
# marks and percentage.
m = 90
p = 67
c = 87
h = 98
e = 88
totalMarks = m + p + c + h + e
print("Total marks = ",totalMarks)
per = (totalMarks * 100) / 500
print("percentage of all marks = ",per)


# Q.5 Write a program for swapping of two integer variables using third variable.
a = 10
b = 20

temp = a
a = b
b = temp
print("the value of a = ",a,"\nthe value of b is = ",b)


# Q.6 Write a program for swapping of two integer variable without third variable.
a = 10
b = 20

a = a + b
b = a - b
a = a - b
print("the value of a = ",a,"\nthe value of b is = ",b) 

# Q.7 Write a program accepts a character and find out corresponding ASCII value.
n  = str(input("Enter a any charcter = "))
a = ord(n)
print("the ASCII vlaue is = ",a) 

# Q.8 Write a program to calculate sum of digits number.(Hint:-123 is a given number then o/p=6)
n =int(input("enter a any three digit number = "))
sum = 0
temp = n % 10
sum = sum + temp
n = n // 10

temp = n % 10
sum = sum + temp
n = n // 10

temp = n % 10
sum = sum + temp
n = n // 10
print(sum)


# Q.9 Write a program accepts 4 digits no. and display the no. in reverse order.
n =int(input("enter a any three digit number = "))
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

temp = n % 10
revNum = revNum * 10 + temp
n = n // 10
print(revNum)

# Q.10 Write a program accepts an amount in rupees (Hint Rs 4567) and find out how many currency of
Rs 2000,500,200,100,50,20,10,5,2,1.
temp  = 0
remAmt = 0
sum = 0
amount = int(input("enter your amount = "))
temp = amount // 2000 
remAmt = amount % 2000 
print("the total notes of 2000 be used in your amount = ", temp)

temp = remAmt // 500
remAmt = remAmt % 500
print("the total notes of 500 be used in your amount = ", temp)

temp = remAmt // 200
remAmt = remAmt % 200
print("the total notes of 200 be used in your amount = ", temp)

temp = remAmt // 100
remAmt = remAmt % 100
print("the total notes of 100 be used in your amount = ", temp)

temp = remAmt // 50
remAmt = remAmt % 501
print("the total notes of 50 be used in your amount = ", temp)

temp = remAmt // 20
remAmt = remAmt % 20
print("the total notes of 20 be used in your amount = ", temp)

temp = remAmt // 10
remAmt = remAmt % 10
print("the total notes of 10 be used in your amount = ", temp)

temp = remAmt // 5
remAmt = remAmt % 5
print("the total notes of 5 be used in your amount = ", temp)

temp = remAmt // 2
remAmt = remAmt % 2
print("the total notes of 2 be used in your amount = ", temp)

temp = remAmt // 1
remAmt = remAmt % 1 
print("the total notes of 1 be used in your amount = ", temp)


# Q.11 Write a program accepts three numbers from user and calculate average of given three numbers.
num1 = int(input("Enter a first number = "))
num2 = int(input("Enter a first number = "))
num3 = int(input("Enter a first number = "))
avg = (num1 + num2 + num3) / 3
print(avg)

#Q.12 calculate Area of square 
side = int(input("Enter a side of a square = "))
Area = side * side 
print("Area of square = ",Area)

#Q.13 find circumference of circle 
r = float(input("Enter a radius of circle = "))
circum = 2 * 3.14 * r
print("circumference of circle = ",circum) 

#Q.14 print hello world 
print("Hello_World") 

#Q.15 find Area of rectangle 
l = int(input("Enter a length of rectangle = "))
b = int(input("Enter a breadth of rectangle = "))
Area = l * b
print("Area of rectangle is = ",Area) 

#Q.16 find parameter of recteengle 
l = int(input("Enter a length of rectangle = "))
b = int(input("Enter a breadth of rectangle = "))
para = 2 * (l + b)
print("parameter of rectangle is = ",para)

# Q.17 Built a calculator____
a = int(input("Enter a value of a = "))
b = int(input("Enter a value of b = "))
print("sum of a + b = ",(a+b))
print("subtraction of a - b = ",(a-b))
print("multiple of a * b = ",(a*b))
print("division a // b = ",(a//b))
print("modulus a % b = ",(a%b))
'''



