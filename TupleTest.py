'''

Read only
caching
Once created cannot change
use index
you cannot add, remove, delete element from Tuple
'''

sampleTuple = ("Rose","zinnia","hibiscus")
print(sampleTuple)

# index
print(sampleTuple[2])

# iteration
for eachitem in sampleTuple:
    print(eachitem)

if "begonia" in sampleTuple:
    print("Begoinia exists in Tuple")
else:
    print("Begoina doesn't exists")

print(len(sampleTuple))
del sampleTuple