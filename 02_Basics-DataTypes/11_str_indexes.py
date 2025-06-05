# Every string have a indexed base value (like this)

# 'me me me'
#  01234567

strIndexes = 'me me me'

# Find a character between a string using this Rule
# [start:stop:stepover] StepOver Means how many characters to skip
print(strIndexes[0:8:2]) # it will print 'm e'

numbers = '0123456789'


#Guess the output of each print statement before you click RUN!
print('Examples:')

print(numbers[:10])
print(numbers[::1]) # this is step over only
print(numbers[-3]) # its read reversable
print(numbers[::-1]) # its reverse the string by stepover

print(numbers[1:4])
print(numbers[1:])
print(numbers[:])
print(numbers[1:100])
print(numbers[-1])
print(numbers[-4])
print(numbers[:-3])
print(numbers[-3:])
print(numbers[::-1])