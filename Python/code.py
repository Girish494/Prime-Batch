# print("hello world")
# # variables
# name="girish"
# age=21
# PI=3.14
# isPrime=True
# print(name,age,PI)
# identifiers are case sensitive
#data types
# integer,string,float,boolean,None
# print(type(name))
# print(type(age))
# print(type(PI))
# print(type(isPrime))
# a=5
# b=10
# sum=a+b
# print(sum)
#operators 
'''Arithmetic,relational,assignment,logical'''
# type conversion-implicit
# type casting-explicit     
# user input
# a=input("enter value of a ")
# print(a)
'''num_1=int(input("enter number 1: "))
num_2=int(input("enter number 2: "))
avrg=(num_1+num_2)/2
print("AVERAGE : ",avrg)
'''
# color=input("enter your color ")
# if (color=="Red"):
#     print("stop")
# elif (color=="Green"):
#     print("go")
# elif(color=="yellow"):
#     print("look")    
# else:
#     print("wrong color for traffic light")

# age=int(input("enter your age "))
# if(age<13):
#     print("child")
# elif(age>=13 and age<=18):
#     print("teenager")    
# elif(age>18):
#     print("adult")    
# num=int(input("enter the number "))
# if(num%2==0):
#     print("even")
# else:
#     print("odd")    
# username=input("enter username ")
# password=input("enter pasword  ")
# if(username=="admin"and password=="pass"):
#     print("sucess")
# else:
#     if(username!="admin"):
#         print("wrong username")
#     else:
#         print("wrong password")    
# match case
# color=input("enter color ")
# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Look")
#     case "Red":
#         print("Stop")        
#     case _:
#         print("Wrong color")    

# loops
# i=1
# # num=int(input("enter table number "))
# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# string="aeiou"
# ans=0
# for var in string:
#     if(var=="a" or var=="e" or var=="i" or var=="o" or var=="u"  ):
#         ans+=1
# print(ans)
# for i in range(1,10,2):
#     print(i)
# num=int(input("enter the number "))
# ans=0
# for i in range(1,num+1):
#     ans+=i
   
# print(ans)    
# def calling():
#     print("hello")

# calling()
# 
# num1=int(input("enter number 1 "))
# num2=int(input("enter number 2 "))
# num3=int(input("enter number 3 "))

# def avg(num1,num2,num3):
#     ans=(num1+num2+num3)/3
#     return ans
# print(avg(num1,num2,num3))
# sum=lambda a,b:a+b
# print(sum(1,2))
# num=int(input("Enter number "))
# ans=1
# for i in range (1,num+1):
#     ans*=i

# print(ans)

# def factorial(num):
#     ans=1
#     if(num==0):
#         return ans

#     for i in range(1,num+1):
#         ans*=i
#     return ans    
# print(factorial(0))
    
'''assignment problems'''
# 1.
# salary=int(input("enter your salary "))
# if(salary<30000):
#     print(salary*0.05 ,"is the final rate tax on 5%")
# elif (salary>=3000 and salary<=70000):
#     print(salary*0.15,"is the final rate tax on 15%")    
# else:
#     print(salary*0.25,"is the final rate tax on 25%")    
# 2.
# def even(num1,num2):
#     for i in range(num1,num2+1):
#         if(i%2==0):
#             print(i)
# even(1,6);        
# 3.
# def numPrint(num):
#     if(num==0):
#         return 
#     lastDigit=int(num%10)
#     num=int(num/10)
#     numPrint(num)
#     print(lastDigit)
# print(numPrint(312))    
# num=10203040504
# count=0
# while(num>0):
#     if(num%10!=0):
#         count+=1
#     num=int(num/10)
# print(count)        
def numCount(num):
    count=0
    while(num>0):
        if(num%10!=0):
            count+=1
        num=int(num/10)

    print(count)        
numCount(000)