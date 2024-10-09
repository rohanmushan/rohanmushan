# Check if a list is sorted in ascending order
# Function to check if a list is sorted in ascending order
def is_sorted_ascending(input_list):
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[i - 1]:
            return False
    return True

# Sample list
my_list = [1, 2, 3, 4, 5]

# Check if the list is sorted in ascending order
if is_sorted_ascending(my_list):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")
