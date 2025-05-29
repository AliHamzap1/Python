# List

print('LIST in python are used to store multiple datatype in single variable, we access them based on indexes.')
print('LISTs are mutable, means it can be change according to indexes. We add and remove value between in LISTs.')

print('\n Resources: \n')
print('https://www.w3schools.com/python/python_ref_list.asp')

list_var = ['String', 1 , 0.1, True, 'etc']

print(list_var[2])
print(list_var)



print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

print('List Slicing')
print('Rule: list_var[start:stop:stepover]')

BookShelf = ['Maths', 'Chemistry', 'Physics', 'Biology']
BookShelf[3] = 'Computer Science'

print(BookShelf[0:]) #this create a new list
print(BookShelf)    # this list is remain old.

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

Cart = ['Handwash', 'Dishwash', 'Wipes', 'Tissue']
newCart = Cart[:] #this create new copy 
newCart = Cart # this modified previous list
newCart[0] = 'Shampo'

print(newCart[0:]) #this create a new list
print(Cart)    # this list is remain old.


print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

basket = [1,2,3,4,5]

# Adding

# new_list = basket.append(6) #append does not create a new list its just modify list
basket.append(6) # Add value at the last on the list
print(basket)

basket.insert(6, 7) # Add value on the basis on index
print(basket)

basket.extend([8]) # add multiple value on the end.
print(basket)

# Remove
print('Pop return process value so it create a new list.')
print('remove doesn\'t return process value so it can not create any list, it just modify list.')

basket.pop() # just remove the last value
print(basket)

basket.pop(6) # remove the the using index number
print(basket)

basket.remove(6) # remove value from list remove('value from list') like 1 or 'Ali'
print(basket)

basket.clear() # clear remove  all values from list.
print(basket)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

print('Python Keywords')
print('Web Link: https://www.w3schools.com/python/python_ref_keywords.asp')
keywords = ['a', 'b', 'c', 'd', 'e', 'f', 'd', 'x']

print('c' in keywords) # (Return TRUE or FALSE) find something in any string
print(keywords.count('f')) # (Count given string) count string or integer

# keywords.sort() # Sort array
# print(keywords)

sorted(keywords) # it always created new LIST so print new list using a new variable
print(sorted(keywords))

slice_keywords = keywords[:] # this created a copy as per our requirment
copy_keywords = keywords.copy()

keywords.reverse() # it reverse the array (change values on opposite index                                                         )
print(keywords)

range1299 = range(1,100) # it create 1 to 99
range0299 = range(100) # it create 0 to 99
numlist = list(range0299)
print(numlist)


# JOIN a LIST with any STRING

sentence = ''.join(['Hi,', 'My', 'name', 'is', 'Ali', 'Hamza'])



# LIST Unpacking (its like multiple string assigning)
a, b, c, *remaining, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(remaining)
print(d)