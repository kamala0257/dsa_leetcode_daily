#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # Check for each required character type
    has_digit = any(c.isdigit() for c in password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    
    special_characters = "!@#$%^&*()-+"
    has_special = any(c in special_characters for c in password)
    
    # Count how many criteria are missing
    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower: 
        missing_types += 1
    if not has_upper: 
        missing_types += 1
    if not has_special: 
        missing_types += 1
    
    # Check how many characters are needed to reach the minimum length of 6
    length_deficit = max(0, 6 - n)
    
    # The answer is the maximum of missing character types and length deficit
    return max(missing_types, length_deficit)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
