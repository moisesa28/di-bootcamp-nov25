# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).

# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.


number = int(input('Type in a number '))

length = int(input('Choose a lenght '))

multiples = []
for i in range(1, length +1):
    multiples.append(number * i)
    print(multiples)
   


# Challenge 2: Remove Consecutive Duplicate Letters
#1. Ask the user for a string.

word = str(input('Type the word Calaabbaazzaaa \n'))


    
