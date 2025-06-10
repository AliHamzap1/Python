# Python Built-in Functions (or Methods)

greet = 'hellloooo, this is a sample text.'
cap_text = 'CAPITALIZE TEXT to lower case.'

print(len(greet))               # find lenght of any character

print(greet[0:len(greet)])      # slicing the string

print(greet.upper())            # convert to upper case
print(greet.capitalize())       # convert first letter to upper case
print(cap_text.lower())         # convert to lower case
print(greet.find('sample'))     #this return the index of string

# replace('new_word', 'oldWord')
print(greet.replace('hellloooo', 'hey'))

# This can not change the string, it generate new string. Because string can not be changed. Strings are immutable.