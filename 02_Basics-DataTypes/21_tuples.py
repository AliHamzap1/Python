# Tuple

print('Tuples are immutable (Can not be changed).')
my_tuple = (1,2,3,4,5,6,7,8,9)

print(my_tuple[2]) # find based on index number

print(8 in my_tuple) # find Value Tuple

print(my_tuple.index(4)) # find Index of a value

print(my_tuple.count(4)) # find Index of a value


a,b,c, *other, d = (1,2,3,4,5,6,7,8,9)

print (a)
print (b)
print (c)
print (d)
print (other)