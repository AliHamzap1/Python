print('Sets are simply unordered collection of unique objects.')

# set just store unique values it not support indexing
sample_set = {1,2,3,4,5,5}
print(sample_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')



my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# difference
print(my_set.difference(your_set))

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# discard
print(my_set.discard(5))
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# difference_update
print(my_set.difference_update(your_set))
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# difference_update
print(my_set.difference_update(your_set))
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# intersection
print(my_set.intersection(your_set))
print(my_set & your_set) # second way to find intersaction
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# isdisjoint (This Checks, Is there any common value? then return False, otherwise return TRUE)
print(my_set.isdisjoint(your_set))
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# isdisjoint (This Checks, Is there any common value? then return False, otherwise return TRUE)
print(my_set.isdisjoint(your_set))
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# union
print(my_set.union(your_set)) # it create a new set using merge both sets and skip  
print(my_set | your_set) # second way to find union
print(my_set)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
# issubset
print(my_set.issubset(your_set)) #{4,5} is subset of your_set

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

print(your_set.issuperset(my_set)) # your_set is issuperset of my_set