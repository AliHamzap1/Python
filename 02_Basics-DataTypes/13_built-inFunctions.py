greet = 'hellloooo, this is a sample text'

print(len(greet)) # find lenght of any character

print(greet[0:len(greet)])

print(greet.upper())
print(greet.capitalize())
print(greet.lower())
print(greet.find('is')) #this return the index of string

# replace('new_word', 'oldWord')
print(greet.replace('hellloooo', 'hey'))

# This can not change the string, it generate new string. Because string can not be changed.