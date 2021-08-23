'''
Question 2:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
1.	If the number is a multiple of 4, print out a different message.
2.	Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

num1 = str(input("Enter two numbers.  Enter first number  :  "))
num2 = str(input("Enter the second number   :   "))
if num1.isdigit():
    if int(num1)% 2 == 0:
        print(num1 , " is a even number.")
        if int(num1) >=4 and int(num1) % 4 ==0:
            print( num1, " is a multiple of 4.")
        else:
            print( num1 , " is not a multiple of 4.")
    else:
        print(num1 , "  is a odd number.")

else:
    print("Invalid number.")

numerator = int(num1)
denominator = int(num2)

if (str(numerator).isdigit() and str(denominator).isdigit()):
    answer = numerator / denominator
    if (numerator % denominator) == 0:
        print(" Denominator completely divides the numerator  and the answer is ", answer )
    else:
        print("  Denominator does not completely divides the numerator and the answer is ", answer)
else:
    print("Invalid numbers")
