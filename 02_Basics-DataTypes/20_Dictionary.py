# Dictionary

Num_Dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

print(Num_Dict)

Mix_Dict = {
    'a' : [1,2,3],
    'b' : 'Hellooow',
    'c' : True
}
print(Mix_Dict)

print('Making List of Dictionaries')

Dict_List = [
    {
        'a' : 1,
        'b' : 2,
        'c' : 3
    },
    {
        'a' : [1,2,3],
        'b' : 'Hellooow',
        'c' : True
    }
]

print(Dict_List[0]['c'])
print(Dict_List[1]['a'])


# Dicionary Keys
print("\n DICTIONARIES keys are immutable, we use int, float, tuple for assign keys but we are not assign LIST for making key.")

sameStrKey_Dict = {
    'a' : [1,2,3],
    '100' : 'Hellooow',
    '100' : True
}
print(sameStrKey_Dict['100']) # Now 100 take new value and OLD STR key is no more.

# listKey_Dict = {
#     'a' : [1,2,3],
#     'b' : 'Hellooow',
#     {100} : True
# }# list can not be work because its key in [LIST] format.


print('\n Interpreter generate an error when you print an Element from a DICTIONARY which is not exist. Lets see this')

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    # 'age': 30
}
print(user.get('age', '25'))  # Returns None since 'age' key does not exist aslo define a default value


print('\n There is also another way to write create DICTIONARY which is mot common.')
user2 =  dict(name="Ali Hamza")
print(user2)
print(user2['name'])


# Find Key in Dictionaries
finding = {
    'basket': [1,2,3],
    'name': 'Ali Hamza',
    'age': 24
}

print('\n\n\n')

print('age' in finding.keys()) # find any key in dictionary
print('Ali Hamza' in finding.values()) # find any Values in dictionary

print(finding.items()) # show all items in dictionary

# copy dictionary
finding2 = finding.copy()
print(finding2)

# Clear all items indictionary
finding.clear()
print(finding) # Now Dictionary is NONE


print('\n\n\n')

# POP clear GIVEN key and Value from Dictionary
pop_dict = {
    'languages': ['PHP', 'Pyhton', 'JS'],
    'name': 'Ali Hamza',
    'age': 24
}
print(pop_dict.pop('age')) # it return deleted value
print(pop_dict)


print('\n\n\n')

# POP clear LAST key and Value from Dictionary
popItems_dict = {
    'languages': ['PHP', 'Pyhton', 'JS'],
    'name': 'Ali Hamza',
    'age': 24,
    'languages2': ['PHP', 'Pyhton', 'JS'],
    'name2': 'Ali Hamza'
}
print(popItems_dict.popitem()) # it return deleted key and value
print(popItems_dict)


print('\n\n\n')

# UPDATE ADD or UPDATE Key's Value
update_dict = {
    'languages': ['PHP', 'Pyhton', 'JS'],
    'name': 'Ali Hamza',
    'age': 24,
    'languages2': ['PHP', 'Pyhton', 'JS'],
    'name2': 'Ali Hamza'
}
print(update_dict.update({'name2': 'Ali Esren'})) # it return deleted key and value
print(update_dict)




print('\n Heads up! As of Python 3.7, they have updated this data structure to now have order maintained now. You can read about it here. https://medium.com/junior-dev/python-dictionaries-are-ordered-now-but-how-and-why-5d5a40ee327f')
print('\n However, keep in mind that dictionaries from a programming perspective have usually been unordered (and most other languages have dictionaries that are unordered).')
