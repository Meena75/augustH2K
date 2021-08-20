'''

def function_name(parameters <optional.):
    body of the function
    processing logic
    <option> return
'''

def say_hello(name = "Guest"):
    print("Hello  ",name)

say_hello()
say_hello("Meena")
say_hello(name ="Seenu")

def validation(cust_id,cust_name,cust_zipcode):
    validation_flag= True
    print(cust_id,cust_name,cust_zipcode)
    if str(cust_id).isnumeric():
        int_custid = int(cust_id)
        print ("cust_id is valid and numeric")
    else:
        print("Invalid cust_id")
        validation_flag= False

    if not str(cust_name).isalpha():
        validation_flag = False
        print(" Cust_name is invalid and special character")
    else:
        print("valid cust_name. It has aphabetic")

    if not (str(cust_zipcode).isdigit() and len(str(cust_zipcode)) == 5):
        print("InValid Zipcode")
        validation_flag = False
    else:
        print("valid cust_zipcode")

    return validation_flag


is_valid = validation("1000A","Meena$", "3434567")
print("Is_Valid True for Meena$  =", is_valid)


is_valid = validation("12333","yoges","h3434")
print("Is_Valid True  for yoges =", is_valid)

#validation(cust_id ="20002", cust_zipcode = "34567", cust_name = "Aiswarya")



