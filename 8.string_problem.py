#FIRST PART ==>> Example -->   A = "Why fit in, When you are Born to Stand out!"
'''                 
#(1.) Write a program to find the length of the following sring.
a = "Why fit in , When you are Born to Stand Out"
print(a)
print(len(a)) 

#(2.) Write a program to check how many time alphabet 'o' is occuring.
a = "Why fit in , When you are Born to Stand Out"
print(a.count("o"))   

#(3.) Write a program to convert the whole string into lowerCase and upperCases.
a = "Why fit in , When you are Born to Stand Out"
print(a.upper())
print(a.lower())   

#(4.) Write a program to converrt te following string innto a title.
a = "Why fit in , When you are Born to Stand Out"
print(a.title())  

#(5.) Write a program to find the index number of "fit in".
a = "Why fit in , When you are Born to Stand Out"
print(a.index("fit in"))   '''

#=================================================================================================================================== 
#SECOND PART ==>> Example -->   A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"

'''#(1.) Write a program to separate the following string into comma(,) separated value__
a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(a.split("."))    '

#(2.) Write a program to sort strings alphabetically in python.
a = input("Enter anything here : ")
b ="OOTD.YOLO.ASAP.BRB.GTG.OTW"
c = sorted(a)
d = b.replace(".","")
print(c)
print(sorted(d))     

#(3.) Write a program to remove a given character from a string.
a = "Hello World"
b = a.replace("l","")
print(b)  

#(4.) Write a program to remove dot(.) from the following string.
a = "F.R.I.E.N.D.S."
print(a.replace(".",""))    

#(5.) Write a program to check the number of occurance of a substring in a string.
a = "she sells seashells on the sea shore"
b = a.count("sea")
print("The number of times substring sea is occuring is = ",b) '''

#=========================================================================================================================
# THIRD PART ====>>

'''#(1.) Take an input from a user as a string then , reverse it.
a = input("Enter  anything here = ")
print(a[ : : -1])  

#(2.) Write a program to check if a string contins only digits.
a = input("Enter anything here : ")
b = a.isdigit()
if b == True :
  print("it contain only digit :",a) 
else :
    print("it not contain only digit :",a)  
    

#(3.) Write a program to check if a string is palindrone.
a = input("Enter anything here : ")
b = a
print(a[ : :-1])
if b == a :
    print("Your enter string is palindrone :",b)
else :
    print("Your string is not a palindrone : ",b)    


#(4.) Write a program to find number of vowels in a string.
a = "My name is Abhishek Dwivedi"
vowels = 0
for i in a :
    if ((i == "a" or i == "e" or i == "i" or i == "o" or i == "u" ) or (i == "A" or i == "E" or i == "I" or i == "O" or i == "U")) :
         vowels += 1
print("The number are vowels are : ",vowels)       
  
    
#(5.) Write a program to check if every word in a string begins with a capital letter. 
a = "My name is Abhishek Dwivedi and my father name is Devmurat dwivedi
"
b = a.istitle()
if b == True :
    print("It string begins with a capital letter :",b)
else :
    print("It string not begins with a capital letter :",b)    '''

#====================================================================================================================

 


             

