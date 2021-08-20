# Lists are written with square brackets.

sampleList = ["apple",'orange',"banana",'grapes',"pineapple"]
print (sampleList)
print(sampleList[3])

#Add - Append()
sampleList.append("kiwi")
print(sampleList)

# Add in particular position - insert() moves the rest to the next position
sampleList.insert(2,"guava")
print(sampleList)

# Add duplicates- append
sampleList.append("banana")
print(sampleList)

#Remove - remove()
sampleList.remove("kiwi")
print(sampleList)

# Length - len()
print("Length of the list  :" ,len(sampleList))

#iteration - for loop

for eachitem in sampleList:
    print(eachitem)

#Membership operator

if "coconut" in sampleList:
    print ("coconuts are listed")
else:
    print("coconut is not in the list")

# sort
print(sampleList.sort())

# clear
sampleList.clear()
print(sampleList)

#delete

del sampleList
# print(sampleList) throws error because there is no sampleList List exists. It is wiped off from memory location

