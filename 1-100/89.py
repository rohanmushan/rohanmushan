# Check if a list is a subset of another list.
# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5]

# Check if list2 is a subset of list1 using the issubset() method
is_subset = set(list2).issubset(set(list1))

if is_subset:
    print("list2 is a subset of list1.")
else:
    print("list2 is not a subset of list1.")

#OR

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5]

# Check if list2 is a subset of list1 using sets
is_subset = set(list2).issubset(set(list1))

if is_subset:
    print("list2 is a subset of list1.")
else:
    print("list2 is not a subset of list1.")
