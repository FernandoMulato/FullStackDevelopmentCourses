# Dictonaries
# Syntax of a dictionary
dcty_microsoft_office = {
    # key -- Value
    "word" : "Microsoft Word is the suite’s word processor",
    "excel" : "Microsoft Excel is a spreadsheet program",
    "power" : "Microsoft PowerPoint is a program to develop and deploy visual presentations"
}

# Call an entire dictionary
print(dcty_microsoft_office)

# Call a value from a dictionary element
print(dcty_microsoft_office["word"])

# Dictionary keys with integers
dictionary = {
    1 : "Value 1",
    2 : "Value 2",
    3 : "Value 3"
}

print(dictionary[3])

# Add new items to the dictionary
dcty_microsoft_office["outlook"] = "Microsoft Outlook is a personal information manager and email client"

print(dcty_microsoft_office["outlook"])

# Example of inventory dictionary
dcty_inventory = {
    1 : "Sword",
    2 : "Shield",
    3 : "Health Regenerator"
}

dcty_inventory = {}

print(dcty_inventory)

# Edit existing items in dictionaries
dcty_microsoft_office["word"] = "Microsoft Word is used to write all types of text documents"

print(dcty_microsoft_office["word"])

# Dictionary key iterator loop
for i in dcty_microsoft_office:
    print(f"- {i.capitalize()}") # capitalize(): serves to capitalize the first word without affecting the original format

# Iterating dictionary values with blucles
for i in dcty_microsoft_office:
    print(f"- {i.capitalize()} : {dcty_microsoft_office[i]}")

# sets: are cluttered lists with no position index
st_animals = {"dog", "iguana", "cat", "python", "chimpanzee"}
print(st_animals)

# Duplicate values in the sets
st_animals = {"dog", "iguana", "cat", "python", "chimpanzee", "dog"}
print(st_animals)