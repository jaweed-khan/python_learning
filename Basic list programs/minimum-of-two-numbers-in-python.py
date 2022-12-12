# python program to find the
# minimum of two numbers

# Examples

# Example 1
# Input: a = 2, b = 4
# Output: 2

# Example 2
# Input: a = -1, b = -4
# Output: -4

def minimum(a, b):

    if(a <= b):
        return a
    else:
        return b

# Driver code
a = 2
b = 4
print(minimum(a, b))