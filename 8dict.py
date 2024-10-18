# Create a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Print the original dictionary
print("Original dictionary:", my_dict)

# Add a new key-value pair
my_dict['job'] = 'Engineer'
print("After adding job:", my_dict)

# Update an existing key-value pair
my_dict['age'] = 31
print("After updating age:", my_dict)

# Remove a key-value pair
del my_dict['city']
print("After removing city:", my_dict)

# Check if a key exists
print("Is 'name' in dictionary?", 'name' in my_dict)
print("Is 'city' in dictionary?", 'city' in my_dict)

# Set operations
print("\nSet Operations:")

# Create a set
my_set = {1, 2, 3, 4, 5}

# Print the original set
print("Original set:", my_set)

# Add an element to the set
my_set.add(6)
print("After adding 6:", my_set)

# Remove an element from the set
my_set.discard(3)  # discard does not raise an error if the element is not present
print("After removing 3:", my_set)

# Check if an element is in the set
print("Is 4 in the set?", 4 in my_set)
print("Is 10 in the set?", 10 in my_set)

# Union and intersection of sets
another_set = {4, 5, 6, 7, 8}
print("Another set:", another_set)

union_set = my_set | another_set
print("Union of sets:", union_set)

intersection_set = my_set & another_set
print("Intersection of sets:", intersection_set)
