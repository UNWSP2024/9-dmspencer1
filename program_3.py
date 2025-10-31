# Title: Average Numbers
# Author: Dalila Spencer
# Date: 2025-10-30

# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################

    try:

        infile = open('numbers.txt', 'r')

        total = 0.0

        for line in infile:
            amount = float(line)
            total += amount

        infile.close()

        print(f'The total of the numbers in numbers.txt is: {total:,.2f}')

    except ValueError:
        print('ERROR: invalid number found in numbers.txt')

    except IOError:
        print('ERROR: file not found')

    ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()