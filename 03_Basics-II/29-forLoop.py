# For Loop

# for variableName in iteration:

# it works with string
for itemS in "Ali Hamza":
    print(itemS)

# it works with list
for itemL in [1,2,3]:
    print(itemL)


# it works with set
for itemSet in {1,2,3}:
    print(itemSet)

# it works with tupal
for itemT in {1,2,3}:
    print(itemT)

print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

# Now see this can you able to 
for itemL in [1,2,3]:
    print(itemL)
    print(itemL)
    print(itemL)

print(itemL) # this variable contain the last value which is store at the end of loop


print('\n ---------------------------------------------------------------------------------------------------------------------------- \n')

for itemsMain in [1,2,3]:
    for itemsNest in ['a', 'b', 'c']:
        print(itemsMain, itemsNest)