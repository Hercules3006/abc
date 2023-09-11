def remove_duplicates(input_dict):
    unique_values = {}  # Create a new dictionary to store unique values

    for key, value in input_dict.items():
        if value not in unique_values.values():
            unique_values[key] = value  # Add the key-value pair if the value is unique

    return unique_values

# Example dictionary with duplicate values
input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Remove duplicate values
result_dict = remove_duplicates(input_dict)

print(result_dict) 