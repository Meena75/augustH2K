'''
Three number comparison to find the biggest
'''

first = int(input("Enter the first number  :"))
second = int(input("Enter the second number  :"))
third = int(input("Enter the third number  :"))
four = int(input("Enter the fourth number  :"))

if (first > second) and (first > third) and (first > four):
    print(" First number is the biggest  : ",first)
elif (second > third) and (second > four):
    print(" Second number is the biggest  : ", second)
elif (third > four):
    print(" Third number is the biggest  : ", third)
else:
    print(" Fourth number is the biggest  : ", four)


