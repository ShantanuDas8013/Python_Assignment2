def merging_Dict(*args):
    """Merge multiple dictionaries into one."""
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys_set &= set(dictionary.keys())
    return common_keys_set

def invert_dict(dictionary):
    """Invert a dictionary by swapping keys and values. If multiple keys have the same value, group them in a list."""
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
    return inverted_dict

def main():
    
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'d': 4, 'e': 2, 'f': 6}
    dict3 = {'g': 1, 'h': 5, 'i': 6}
    
    print("Merging Dictionaries:")
    merged = merging_Dict(dict1, dict2, dict3)
    print("Merged Dictionary:", merged)
    
    print("\nCommon Keys in Dictionaries:")
    common_keys_set = common_keys(dict1, dict2, dict3)
    print("Common Keys:", common_keys_set)
    
    print("\nInverting Dictionary:")
    inverted = invert_dict(merged)
    print("Inverted Dictionary:", inverted)

if __name__ == "__main__":
    main()
