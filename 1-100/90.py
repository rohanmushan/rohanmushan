# Find the mode (most frequent element) in a list.

def find_mode(input_list):
    element_count = {}
    
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    max_count = max(element_count.values())
    mode_elements = [element for element, count in element_count.items() if count == max_count]

    return mode_elements

# Sample list
my_list = [1, 2, 2, 3, 4, 4, 4, 5, 5]

# Find the mode(s) in the list
mode_elements = find_mode(my_list)

# Print the mode(s)
print("Mode(s) in the List:", mode_elements)
