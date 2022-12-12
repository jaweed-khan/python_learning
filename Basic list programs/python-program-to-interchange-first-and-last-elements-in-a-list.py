# python 3 program to swap first
# and last element of a list

# Examples

# Example 1
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Example 2
# Input : [1, 2, 3]
# Output : [3, 2, 1]

def swaplist(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

newList = [12, 35, 9, 56, 24]

print(swaplist(newList))