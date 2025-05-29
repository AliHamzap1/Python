# Create a password checker

username = input('What is your Username?\n')
password = input('What is your password?\n')

password_length = len(password)

password_hash = password_length * '*'

print(f'Hey {username}, Your password, {password_hash} is {password_length} letters long.')