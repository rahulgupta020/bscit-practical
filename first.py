'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year 
that they will turn 100 years old'''

import datetime
name=input("Enter your name :- ")
age=int(input("Enter your age :- "))
currentyear=datetime.datetime.now().year
dob=currentyear - age
print(dob+100)


''''age=22
current year=2020
2020-22=1998
dob=1998
1998+100=2098'''