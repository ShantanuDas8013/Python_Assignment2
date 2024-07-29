def add_element(s, element):
    s.add(element)

def remove_element(s, element):
    s.discard(element)

def union(s1, s2):
    return s1 | s2

def intersection(s1, s2):
    return s1 & s2

def difference(s1, s2):
    return s1 - s2

def is_subset(s1, s2):
    return s1.issubset(s2)

def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    return s1 ^ s2

def power_set(s):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def unique_subsets(s):
    return set(power_set(s))


if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}

    add_element(set1, 4)
    remove_element(set2, 5)

    print("Union:", union(set1, set2))
    print("Intersection:", intersection(set1, set2))
    print("Difference:", difference(set1, set2))
    print("Is subset:", is_subset(set1, set2))
    print("Set length:", set_length(set1))
    print("Symmetric difference:", symmetric_difference(set1, set2))
    print("Power set:", power_set(set1))
    print("Unique subsets:", unique_subsets(set1))
