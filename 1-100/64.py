
def merge_sorted_lists(list1, list2):
    merged_list=[]
    i=j=0

    # Iterate through both lists, comparing elements
    while i<len(list1)andj<len(list2):
        if list1[i]<list2[j]:
            merged_list.append(list1[i])
            i+=1
        else:
            merged_list.append(list2[j])
            j+=1

    # Append remaining elements from both lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Sample sorted lists
list1=[1, 3, 5, 7]
list2=[2, 4, 6, 8]

# Merge the two sorted lists
result = merge_sorted_lists(list1, list2)

# Print the merged sorted list
print("Merged Sorted List:", result)
