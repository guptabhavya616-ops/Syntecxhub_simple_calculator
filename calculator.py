import os

#addition
def add(num1,num2):
    return num1+num2

#subtraction
def sub(num1,num2):
    return num1-num2

#multiplication
def multiply(num1,num2):
    return num1*num2

##division
def divide(num1,num2):
    if num2==0:
        return "error , cannot divide by zero"
    return num1/num2

#main calculation function
def calculate(num1, operator, num2):
    
    if operator=="+":
        return add(num1,num2)
    
    elif operator=="-":
        return sub(num1,num2)
    elif operator =="*":
        return multiply(num1,num2)
    elif operator=="/":
        return divide(num1,num2)
    else:
        return"invalid operator"
    
#clear screeen function
def clear_screen():
    os.system("cls"if os.name=="nt" else "clear")
    
#calculator menu
def calculator():
     
     while True:
         print("/n Simple calculator")
         print("1.Calculate")
         print("2. clear")
         print("3, exit")
         
         choice=input("enter your choice : ")
         
         #calculate
         if choice == "1":
             try:
                 num1 = float(input("enter first number"))
                 operator = input(
                     "enter operator (+,-, * , /)"
                 )
                 
                 num2= float(input("enter second number"))
                 result = calculate(num1 , operator , num2)
                 print("result",result)
             except ValueError:
                 print("error please enter valid number")
         #clear
         elif choice =="2":
             clear_screen()
          #exit
         elif choice =="3":
             print("Thank you for using calculator")
             break #for stop the loop
         #invalid menu choice
         else:
             print("error : invalid choice , please select only 1,2 and 3")
#start calculator             
calculator()           
                     
    
            