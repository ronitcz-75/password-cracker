# password cracker using time module the dictnory 

import random as r 
import time as t

admin=input("User name: ")
def s():
     if admin=="admin123":
        print("please wait..")
        print(t.sleep(1))
     else:
        print(t.sleep(1))
        print("user is not found please try again...")
     passw=input("Enter password: ")
     if passw=="admin123":
        print("please wait to verify: ")
        print(t.sleep(1))
        print("valid....")
     else:
         print(t.sleep(1))
         print("invalid try again!!!!")

def point():
   #Targets list with their password in dictonary
    data={"user1":"user1231","user2":"user12203"}
    
    taget=input("enter target: ")
    if taget=="attack":
        print(data)

#Countinue the next process code 

while True:
    s()
    point()
    print("not valid user to continue this process!!!!!")
    break
    
