# Sort a list of dictionaries by a specific key
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 28} ]
sorted_data = sorted(data, key=lambda x: x['age'])
for item in sorted_data:
    print(item)
