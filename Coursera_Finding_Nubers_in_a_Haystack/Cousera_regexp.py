#Instructions
#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#Handling The Data
#The basic outline of this problem is to read the file, look for integers using
#the re.findall(), looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing up the
#integers.
import re
#sample data provided (used list comprehension to solve)
print sum([int(num) for num in re.findall('[0-9]+',open('regex_sum_42.txt').read())])
#my unique data file
print sum([int(num) for num in re.findall('[0-9]+',open('regex_sum_334860.txt').read())])
