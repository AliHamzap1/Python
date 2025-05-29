print('Create a program to check access to driver is it eligible or not.')

is_old = False
is_Licenced = True

# There is no brackets for if and else blocks, we use indents to present blocks.
if is_old and is_Licenced:
    print('You are old enough to drive, and you have a license.')
else:
    print('You are not eligible to drive.')

# Normal IF ElSE Structure
num = 1
if num == 1:
    print(f"Number Equals to {num}")
elif num < 1:
    print("Number is less than 1")
else:
    print(f"Number is {num}")