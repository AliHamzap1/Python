print('Truthy and Falsy Concept')

username = 'Ali'
password = 'Hamza'

# Empty username and Password (if these fields are Null, Output become False)
print(bool(username))
print(bool(password))

# There is no brackets for if and else blocks, we use indents to present blocks.
if username and password:
    print('Username and Password are exist.')
else:
    print('Username and Password are exist.')