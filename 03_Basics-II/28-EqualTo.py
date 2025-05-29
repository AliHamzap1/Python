print('The difference between "==" and "is":')

print('\n == if the objects referred to by the variables are equal. Simply == check equal value. \n')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print('\n "is" will return True if two variables point to the same object (in memory)\n')

print(True is bool(1))
print(True is True)
print('1' is '1')
print([] is []) # because list is data structure and it will completely take new place in memory
print(10 is 10)

print([1,2,3] is [1,2,3])