from datetime import datetime


# Create a program that Guess your age

birth_year = input('What year were you born?')


current_year = datetime.now().strftime('%Y')
age = int(current_year) - int(birth_year)
# print("Your age is " + age + ".")
print(f"Your age is {age}.")