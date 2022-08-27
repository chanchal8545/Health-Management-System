
#exercise 1
#Dictionary
'''dic = {"fruits":"apple", "vegetable":"potato","things":"chair","animal":"lion"}
print(dic)
digit=input()
print(dic[digit])'''


#Exercie 2
#faulty calculater
'''print("Enter the first number")
x = int(input())
print("Enter the second number")
y = int(input())
print("which operation perform")
s = int(input())

if x==56 and y==9 and s ==1:
    print("77") 
elif x==45 and y==3 and s ==3:
    print("555") 
elif x==56 and y==6 and s ==4:
    print("4") 
elif s == 1:
    print(x+y)               
elif s== 2:
    print(x-y)
elif s==3:
    print(x*y) 
elif s==4:
    print(x/y)   '''


#Quiz
'''list= [23,45,67,78,3,5,75,90,float,"chanchal"]

for item in list:
    if str(item).isnumeric() and item >= 6:
        print(item)'''


#while loop
'''i= 0
while (i<45):
    print(i)
    i = i+1   '''



#Quiz         
'''print("Enter the number") 
x = int(input())
while(x<100):
    print("Enter the number")  
    x = int(input())
if (x >= 100):
    print("Congratulation you type a big number")'''



# Exercise 3
# Choose a number

'''n=18
i=1
print("please choose the number")
print("your remaining chances is",5-i,"/5")  
while i<6:
    c=int(input())
    if c<n:
        print("please type biger than it")
    elif c>n:
        print("please type smaller than it")
    elif n==c:
        print("you are right")
        print("your remaining chances is",5-i,"/5\n")  
        break  
    i=i+1     
    print("your remaining chances is",5-i,"/5\n") '''


# Exercise 4 
#print stars
'''print("Enter the number")
n= int(input())
i=0
while i<=n:
      print(" " * (n+1) + " * " * i)
      i=i+1

print("Enter your choice")
t= int(input())
if t==0:
    i=0
    while i<=n:
        print(" " * (n+1) + " * " * i)
        i=i+1
elif t==1:
    n=0
    while i>=n:
      print(" " *(n-1) + " * " * i)
      i=i-1

else :
          print("not allowed")    ''' 



#Function
'''def chanchal(a,b):
     Comment->    this  is a very good sign
    print("Chanchal is a good girl",a+b)
chanchal(5,7)
print(chanchal.__doc__)'''




#pratice
'''print("enter the  number  ")
a= input()
print("enter the number")
b= input()

try: 
   print("the sum of the number",int(a)+int(b))

except Exception as e:
    print(e)

print("this line is very important")'''





'''f=open("chanchal.txt","rt")
#content = f.read()
for line in  f:
     print(line,end="")
#print(content)'''

#2.
'''f=open("chanchal.txt","rt")
print(f.readline())
#content = f.read()
#for line in  content:
  #   print(line)
#print(content)'''


'''f= open("chanchal2.txt","w")
a =f.write(str(input()))
print(a)'''


'''f= open("chanchal2.txt","r+")
print(f.read())
f.write("Thank you")'''



# Exercise 5
#     \\ Health management system
'''
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
            print(content,"[", current_time,"]")'''
 
       
    # Exercise 6 
# Snake water gun

'''import random
list = ["s","w","g"]

total_choice=10
chance=0
my_score=0
computer_score=0

print("\nSnack,Water,Gun Game\n")
print("s for Snack\nw for Water\ng for Gun\n")

while chance<total_choice:
   print("Enter your choice:")
   me=str(input())
   
   r=random.choice(list)
   print("the computer choice is:\n ",r)
   total_choice=total_choice-1
# using snack
   if me=="s" and r=="s":
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",chance,"/10\n")
   elif me=="s" and r=="w":
       my_score=my_score+1
       print("your score is ",my_score,"and computer score is ",computer_score)
       print("you remaining chances is",chance,"/10\n")
   elif me=="s" and r=="g":
       computer_score=computer_score+1
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",chance,"/10\n")

# using water
   if me=="w" and r=="s":
       computer_score=computer_score+1
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="w" and r=="w":
       print("tie both side ")
       print("your score is ",my_score,"computer score is ",computer_score) 
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="w" and r=="g":
       my_score=my_score+1
       print("your score is ",my_score,"and computer score is ",computer_score) 
       print("you remaining chances is",total_choice,"/10\n")

# using gun
   if me=="g" and r=="s":
       my_score=my_score+1
       print("your score is ",my_score,"and computer score is ",computer_score)
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="g" and r=="w":
       computer_score=computer_score+1
       print("your score is ",my_score,"computer score is ",computer_score)
       print("you remaining chances is",total_choice,"/10\n")
   elif me=="g" and r=="g":
       print("tie both side ")
       print("your score is ",my_score,"computer score is ",computer_score)  
       print("you remaining chances is",total_choice,"/10\n")            
print("Game over")
if my_score>computer_score:  
    print("you are the winner and coputer is loose")
elif computer_score>my_score:
    print("coputer is winner and you are loose")   '''                    

# Exercise 7
#Healthy Programmer
# 9am - 5pm
# Water (3.5 litres) - Drank - Every 40 min
# Eyes - every 30 min 
# Physical activity - every - 45 min 
'''
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("alarm.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5 #40*60
    exsecs = 20  #30*60
    eyessecs =  40 #45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'stop' to stop the alarm.")
            musiconloop('alarm.mp3', 'stop')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'stop' to stop the alarm.")
            musiconloop('alarm.mp3', 'stop')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'stop' to stop the alarm.")
            musiconloop('alarm.mp3', 'stop')
            init_exercise = time()
            log_now("Physical Activity done at")'''









  


