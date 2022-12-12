# python program to copy or clone the list
# using a cloning operator

def cloning(li1):
    li_copy = li1[:]
    return li_copy

# Driver code
li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
