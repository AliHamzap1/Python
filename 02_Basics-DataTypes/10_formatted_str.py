# Formatted String
print("Formatted String")

name = "Ali"
age = 24

print('Python 2 way:')
print('Hi, my name is ' + name + ' and I\'m '+ str(age) + ' Years old.')

print('Python 3 way 1:')
print(f'Hi, my name is {name} and I\'m {age} Years old.')       # mostly recommended way in Python 3.6+

print('Python 3 way 2:')
print('Hi, my name is {} and I\'m {} Years old.' .format(name, age) )

print('Assign New Variable:')
print('Hi, my name is {name_new} and I\'m {age} Years old.' .format(name_new = "Hamza", age = 20) )

print('Change Positions of dynamic values:')
print('Hi, my name is {1} and I\'m {0} Years old.' .format(name, age) )