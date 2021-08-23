'''
Question 1:
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
 tells them the year that they will turn 100 years old.
Extras:
1.	Add on to the previous program by asking the user for another number and printing out that many copies of
the previous message. (Hint: order of operations exists in Python)
2.	Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same
as pressing the ENTER button)

'''
import datetime

name = str(input("Enter your name  : "))
age = str(input("Enter your Age   : "))
copies = str(input("Enter the number of times your message to be printed   : "))

x= datetime.datetime.now()
currentyear = int(x.year)

if age.isdigit():
    if int(age) < 1 or int(age) > 100:
        print(" Your age should be above one and below 100")
    else:
        tempage = 100 - int(age)
        finalyear = currentyear + tempage
        for eachcopy in copies:
            print(name, ", you will be 100 years in year ",finalyear)

else:
    print(" Please print your age in numbers")




