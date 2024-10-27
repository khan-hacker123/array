def flatten_array(nested_array):
    flat_array = []
    
    def flatten_helper(arr):
        for item in arr:
            if isinstance(item, list):
                flatten_helper(item)
            else:
                flat_array.append(item)
    
    flatten_helper(nested_array)
    return flat_array

example_input = [1, [2, [3, [4, 5]], 6], 7]
flattened_output = flatten_array(example_input)
print(flattened_output)
