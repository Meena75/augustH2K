'''
Unordered
No Duplicates
'''

sampleSet = {'one','two','three','four','five'}
print(sampleSet)

# Add
sampleSet.add('six')
print(sampleSet)

#Remove
sampleSet.remove("six")
print(sampleSet)

sampleSet.add("eleven")
print(sampleSet)

#Iterate

for eachitem in sampleSet:
    print(eachitem)

# Membership
if ("seven") in sampleSet:
    print("seven present in set")
else:
    print("seven is not present in set")

# clear
sampleSet.clear()
print(sampleSet)

# update
anotherset = {"Meena","veena","Mona","Kona","jolna"}
sampleSet.update(anotherset)
print(sampleSet)

#Discard - If the item is there it will remove otherwise it won't give error

sampleSet.discard("eight")
sampleSet.discard("jolna")
print(sampleSet)