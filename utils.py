from cmath import sqrt
from math import gcd
from functools import reduce

def clean_input(text):
    """
    Clean the text input.
    """
    return ''.join([char for char in text if char.isalpha()]).upper()

def display_output(output):
    """
    Display the output to the user.
    """
    print(output)

def find_gcd_of_list(num_list):
    x = reduce(gcd, num_list)
    return x
