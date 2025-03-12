'''#(1.) Write a program to swap first and fourth element.
my_list = ["Ross","Rachel","Monica","joe"]
temp  = my_list[0]
my_list[0] = my_list[3]
my_list[3] = temp
print(my_list) 

#========================================================================================================
#(2.) wite a program to add a new value at second positon.
my_list = ["Ross","Rachel","Monica","joe"]
my_list.insert(2,"newvalue")
print(my_list)  
 
#===========================================================================================================
#(3.) Write a program to delete a value from 3rd position .
my_list = [13,7,12,10]
my_list.pop(3)
print(my_list) 

#================================================================================================================
#(4.) Write a program to multiply all the numbers in the list.
my_list = [13,7,12,10]
temp = 1

for i in my_list :
    temp *= i
print(temp)  '''

#=================================================================================================================  
'''# (5.) Write a program  to get the largest number from the list.
my_list = [13,7,12,10]
print(max(my_list))
'''
#==================================================================================================================
'''#(6.) Write a program to get the smallest number from the list.
my_list = [13,7,12,10]
print(min(my_list))    
'''
#=========================================================================================================================
