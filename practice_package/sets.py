def find_common_elements(set1, set2):
    common_elements = set()
    for element in set1:
        if element in set2:
            common_elements.add(element)
    return common_elements

def is_superset(set_a, set_b):
    for element in set_b:
        if element not in set_a:
            return False
    return True

def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))

def find_shared_items(*sets):
    shared_items = sets[0]
    for s in sets[1:]:
        shared_items = {item for item in shared_items if item in s}
    return shared_items
