def validation(cust_id,cust_name,cust_zipcode, **kwargs):
    for eachArgs in kwargs:
        print("*Args Handling   :", kwargs.get(eachArgs))


validation("3000","Akshayapriya","23456",address ="6099 braemore", hobby ="drawaing")