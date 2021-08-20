'''

Triangle problem with getting input from the user
'''

side1 = int(input("Enter side 1  :"))
side2 = int(input("Enter side 2  :"))
side3 = int(input("Enter side 3  :"))

check1 = (side1 + side2) > side3
print(check1, ",",side1 , "+",side2,">", side3)
check2 = (side1 + side3) > side2
print(check2, ',', side1, "+", side3, ">", side2)
check3 = (side2 + side3) > side1
print(check3, ",",side2 , "+",side3,">", side1)

Result = check1 and check2 and check3

print("Triangle can be formed with these values  : ", Result)