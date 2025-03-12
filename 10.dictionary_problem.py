'''
#(1.) Write  a python program to sort a dictionary by value.
a = {"a":12 ,"b":23 , "c":6, "d":91 , "e": 45} #This are dictionary items
a =  sorted(a.values())
print(a)
'''
#=================================================================================================================================  
'''
#(2.) Write a python script to print a dictionary where the keys are numbers between 1 and 15 
         and the values are a square of keys.
a = {}
for i in range(1,16) :
    a[i] = i ** 2
print(a)
'''
#=================================================================================================================================  
'''
#(3.) Write a program to multiply all the items in a dictionary.
a = {"a":1 ,"b":2 , "c":3 , "d":4 , "e": 5}
product = 1
for i in a :
    product *= a[i]
print(product)  
'''    
#=================================================================================================================================    
'''
#(4.) Write a python program to sort a dictionary by key.
a = {12:"a" , 56:"b" , 23:"c" , 48:"d" , 91:"e"}
a = sorted(a.keys())
print(a)
'''
#================================================================================================================================= 
'''#(5.) Create a dictionary to store name_of_course (key) and duration_in_month(value). 
# store 5 pairs by default.
courses = { "c_course" : "40_days" , "c++_course": "30_days" , "java_course": "60_days", 
           "python_course": "60_days", "react_course" : "45_days"     
}
print(courses)

#================================================================================================================================= 
#(6.) create a dictionary to store name of cricket teams according to their world rankings.
team_ranking = { 1 : "INDIA" ,
                 2  : "AUSTRALIA" ,
                 3  : "NEWZELAND" ,
                 4  : "SOUTH_AFRICA" ,
                 5  :  "PAKISTAN" ,
                 6  : "AFGANISTAN"  ,   
}
print(team_ranking)

#================================================================================================================================= 
#(7.) Create dictionary to store name of states and 3 cities of each state'
a = { "Madhya_Pradesh" : {"Indore" , "Bhopal" , "Gwalior"} ,
      "Uttar_Pradesh"  : {"Lucknnow" , "Prayagraj" , "Gorkhpur"} ,
      "Rajasthan"      : {"Jodhpur" , "Jaipur" , "Kota"} ,
      "Maharastra"     : {"Mumbai" , "Pune" , "Buranpur"} ,
      "Gujarat"        : {"surat" , "Ahamdabad" ,  "kachh"}     
}
print(a)
'''
#================================================================================================================================= 

 

