'''
Question 3:
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
1.	Instead of printing the elements one by one, make a new list that has all the elements less than 5
 from this list in it and print out this new list.
2.	Write this in one line of Python.
3.	Ask the user for a number and return a list that contains only elements from the original list a
that are smaller than that number given by the user.
'''


usernumber = str(input("Enter a number below 90  :  "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
print("Original List a =  ",a)

def ListValidation(c):
    Validation_flag = False
    for eachitem in range(len(c)):
        x= int(c[eachitem])
        if x < 5:
            b.append(c[eachitem])

        if x == int(usernumber):
             Validation_flag = True
    print(" New List b with elements less than 5 from the original list  : ", b)
    #print("Validation_flag   : ", Validation_flag)
    return Validation_flag

is_valid =ListValidation(a)
#print("is_Valid    :  ", is_valid)
if is_valid:
    print ("The number you entered is present in the orignal list. ")
else:
    print("The number you entered is not present in the orignal list. ")



