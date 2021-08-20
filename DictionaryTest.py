sampleDictionary = {
    "Warm":"Red",
    "Cold":"Baige",
    "Nuetral":"Grey",
    "Common":"Black",
}

print(sampleDictionary)
print(sampleDictionary["Cold"])
print(sampleDictionary.get("Warm"))

# Add - replaces the old value
sampleDictionary["Warm"] = "Blue"
print(sampleDictionary)

# Membership
if "Nuetral" in sampleDictionary:
    print(" Nuetral color is  : ", sampleDictionary.get("Nuetral"))

if "Black" in sampleDictionary.values():
    print(" Black exists in the Dictionary : ", sampleDictionary.get("Common"))

# pop
sampleDictionary.pop("Common")
print(sampleDictionary)

# popitem  - Remove the last item in the list
sampleDictionary.popitem()
print(sampleDictionary)

#iterate with Keys
for eachkey in sampleDictionary:
     print(eachkey, sampleDictionary.get(eachkey))

#iterate with Key-Value pairs

for eachkey, eachvalue in sampleDictionary.items():
    print(eachkey, eachvalue)

# iterate with only values

for eachvalue in sampleDictionary.values():
    print(eachvalue)

# you can even add a list as one of the key value pair in dictionary
sampleDictionary["List_item"] = ["apple", "pineapple", "grapes","lotus"]
sampleDictionary["Cold"]="Yellow"
sampleDictionary["Common"] = "White"
print(sampleDictionary)
