def get_value_from_dict(dictionary, key):
    return dictionary.get(key, "Key not found")

# Sample Input
sample_dict = {"name": "Alice", "age": 30}
key = "name"

# Expected Output: "Alice"
print(get_value_from_dict(sample_dict, key))
