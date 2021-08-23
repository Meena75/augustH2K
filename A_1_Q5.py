'''
Question 5:
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between
the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
1.	Randomly generate two lists to test this
2.	Write this in one line of Python (don’t worry if you can’t figure this out at this point -
we’ll get to it soon)
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=a

print("length of a  :", len(a))
print("length of b  :", len(b))
print("C list contains  : ", c)

for eachB in range(0, len(b)):
    #print(eachB, " B  :  ", b[eachB])
    for eachC in range(0,len(c)):
        print ("c[eachC] = ", c[eachC], " and  b[eachB]  = ", b[eachB])
        if c[eachC] == b[eachB]:
            print("Duplicate item. Don't add in the list")
        else:
            c.append(eachB)




