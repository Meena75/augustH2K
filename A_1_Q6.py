'''
Question 6:
Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)
'''

palinstr= str(input("Enter a Palindrome word  :  "))

def palin(s):
    return s== s[::-1]


is_palindrome = palin(palinstr)

if is_palindrome:
    print (" Yes, ", palinstr ," is a Palindrome")
else:
    print(" No, ", palinstr, " is not a Palindrome")