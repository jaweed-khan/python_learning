# python3 code to demostrate 
# Swap elements in String list
# using replace() + list comprehension

# initializing list
test_list = ['G', 'e', 'e', 'k', 's']

# printing original list
print("The original list is : " + str(test_list))

# Swap elements in String List
# using replace() + list comprehension
res = [sub.replace('G', 'f').replace('e', 'G').replace('-', 'e') for sub in test_list]

# printing result
print("List after performing character swaps : " + str(res))