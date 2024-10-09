# Calculate the average value of elements in a list using a set.
# Sample list
my_list=[10, 20, 30, 40, 50]

# Calculate the average of elements in the list
if len(my_list)>0:
    average=sum(my_list)/len(my_list)
    print(f"Average:{average}")
else:
    print("The list is empty. Cannot calculate the average.")
