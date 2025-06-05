# Python Built-in Functions (or Methods)

greet = 'hellloooo, this is a sample text'

print(len(greet))               # find lenght of any character

print(greet[0:len(greet)])      # slicing the string

print(greet.upper())            # convert to upper case
print(greet.capitalize())       # convert first letter to upper case
print(greet.lower())            # convert to lower case
print(greet.find('is'))         #this return the index of string

# replace('new_word', 'oldWord')
print(greet.replace('hellloooo', 'hey'))

# This can not change the string, it generate new string. Because string can not be changed.