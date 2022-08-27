





#   Health management system

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("[", current_time,"]")

print("please enter 1 for log the data and 2 for retrive the data : ")
first=int(input())
if first == 1:
    print("\n1.Enter 1 for harry ->")
    print("2.Enter 2 for marry ->")
    print("3.Enter 3 for varry ->")
    second = int(input())
    if second == 1:
       print("Harry's file opened")
       print("enter 1 for exercise & enter 2 for food")
       third =int(input())
       if third==1:
            print("Please enter the exercise")
            f=open("harry.txt","w")
            a =f.write(str(input()))
            print("Succesfully loged")
       elif  third==2:
            print("please enter the food")
            f=open("harry2.txt","w")
            b =f.write(str(input())) 
            print("Succesfully food loged")
    elif second == 2:
         print("Marry's file opened")
         print("enter 1 for exercise & enter 2 for food")
         third =int(input())
         if third==1:
            print("Please the exercise")
            f=open("Marry.txt","w")
            a =f.write(str(input()))
            print("Succesfully loged")
         elif  third==2:
            print("please enter the food")
            f=open("Marry2.txt","w")
            b =f.write(str(input())) 
            print("Succesfully food loged")     
        
    elif second==3: 
                 print("Varry's file opened")
                 print("enter 1 for exercise & enter 2 for food")
                 third =int(input())
                 if third==1:
                   print("Please the exercise")
                   f=open("Varry.txt","w")
                   a =f.write(str(input()))
                   print("Succesfully loged")
                 elif  third==2:
                    print("please enter the food")
                    f=open("Varry2.txt","w")
                    b =f.write11(str(input())) 
                    print("Succesfully food loged")  
elif first==2: 
    print("You choose the retrive data")
    print("\n1.Enter 1 for harry ->")
    print("2.Enter 2 for marry ->")
    print("3.Enter 3 for varry ->")
    second = int(input())    
    if second==1:
       print("Harry's file opened")
       print("enter 1 for exercise & enter 2 for food")
       third =int(input())
       if third==1:
            print("you choose the exercise")
            f = open("harry.txt","r")
            content =f.read()
            print(content,"[", current_time,"]")
          

       elif third==2:
            print("you choose the exercise")
            f = open("harry2.txt","r")
            content =f.read()
            print(content,"[", current_time,"]")

    elif second==2:
       print("Marry's file opened")
       print("enter 1 for exercise & enter 2 for food")
       third =int(input())
       if third==1:
            print("you choose the exercise")
            f = open("Marry.txt","r")
            content =f.read()
            print(content,"[", current_time,"]")    

       elif third==2:
            print("you choose the exercise")
            f = open("Marry2.txt","r")
            content =f.read()       
            print(content,"[", current_time,"]")
    elif second ==3:
       print("Varry's file opened")
       print("enter 1 for exercise & enter 2 for food")
       third =int(input())
       if third==1:
            print("you choose the exercise")
            f = open("Varry.txt","r")
            content =f.read()
            print(content,"[", current_time,"]")
       elif third==2:
            print("you choose the exercise")
            f = open("Varry2.txt","r")
            content =f.read()       
            print(content,"[", current_time,"]")








  


