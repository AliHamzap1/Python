# Logical Operators

# > = greater than
# < = Less than
# >= = greater than & equal to
# <= = Less than & equal to
# == = Equals to
# != = Not equal to
# or = any one condition is correct
# and = all condition are correct
# not = this is function and also a logical operator

print('a' > 'A') # Equals to TRUE( because of ASCII values 97 > 65 )

print(1 < 2 < 3 < 4) # return True

print(1 < 2 > 3 < 4) # return False

print(1 < 2 > 3 < 4) # return False


print(not(1==1)) # return False


# Program based on Logical Operators
is_magician = False
is_expert = True

if is_magician and is_expert:
    print('Your are a Master Magician')
# elif is_magician and is_expert == False: # its also a technique
elif is_magician and not is_expert:
    print('You need expertise')
elif not is_magician:
    print('You need magic powers')