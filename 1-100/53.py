# Count the frequency of elements in a list using a dictionary
my_list=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
element_count={}
# Count the frequency of elements in the list
for item in my_list:
    if item in element_count:
        element_count[item] += 1
    else:
        element_count[item] = 1

# for item, count in element_count.items():
#     print(f"{item}: {count}")
