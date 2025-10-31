# Title: Random Number File Writer
# Author: Dalila Spencer
# Date: 2025-10-30

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random


num_of_numbers = int(input('How many random numbers do you want to write to random_number.txt?: '))

if num_of_numbers <= 0 or num_of_numbers > 1000:
    num_of_numbers = input('Please enter a number between 1 and 1000: ')

infile = open('random_numbers.txt', 'w')


for num in range(num_of_numbers):
    infile.write(str(random.randint(1,500)) + '\n')


infile.close()

print(f'{num_of_numbers} random numbers have been written to random_numbers.txt')

