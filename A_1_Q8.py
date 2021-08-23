'''
Question 8: Write a program to generate Fibonacci series,for the first n numbers.It is a series of numbers
 in which each number ( Fibonacci number ) isthe sum of the two preceding numbers.
 The simplest is the series 0, 1, 1, 2, 3, 5, 8, etc.
'''

fibno=str(input("Enter a term up to to which Fibonacci Series will be displayed :"))
n1 ,n2 = 0, 1
count =0
if fibno.isdigit():
   if int(fibno) == 1:
        print(" The Fibonacci series is  : " , n1)
   else:
        while count < int(fibno):
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
else:
    print( "Please enter valid positive numeric numbers")