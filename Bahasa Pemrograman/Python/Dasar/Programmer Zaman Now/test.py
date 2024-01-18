# Sample list of dictionaries
my_list = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 22, 'city': 'Los Angeles'}
]

# Value to be removed
value_to_remove = 30

# Iterate through the list and remove the dictionary with the specified value
for item in my_list:
    if 'age' in item and item['age'] == value_to_remove:
        my_list.remove(item)
        break  # Optional: If you only want to remove the first occurrence, you can break out of the loop

# Display the modified list
print(my_list)
