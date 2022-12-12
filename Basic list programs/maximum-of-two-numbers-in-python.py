
# Python program to find the
# maximum of two numbers

# Examples 
# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1

from re import A


def maximum(a, b):

    if(a >= b):
        return a
    else:
        return b
    
# Driver Code
a = 2 
b = 4
print(maximum(a, b))