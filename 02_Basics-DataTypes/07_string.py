# Normal string
username = "supercoder" 
password = "supersecret"

# These are Long string

long_string = '''
WOW
0 0
---
'''

# String Concatination
print('string concatination:')

first_name = 'Ali'
last_name = 'hamza'

full_name = first_name + ' ' + last_name

print(full_name)


name = "Ali" + " Hamza"     # Ali Hamza

# name = "Ali" + 5            # getting error because we are trying to concatinate string with int



# To fix this we can use str() function
name = "Ali" + str(5)      # Ali5
print(name)