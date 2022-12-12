# python3 program to swap elements
# at given positions

# Examples

# Example 1
#Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
#Output : [19, 65, 23, 90]

# Example 2
# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

from pdb import post_mortem


def swapPositions(list, pos1, pos2):

    print(list)
    print(pos1)
    print(pos2)
    print(list[pos1])
    print(list[pos2])

    list[pos1] = list[pos2]
    list[pos2] = list[pos1]
    return list

List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

print(swapPositions(List, pos1-1, pos2-1))