def duplicate_char(list1, list2, list3):    # Convert input strings to lists of characters
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    duplicates = set1.intersection(set2).intersection(set3)           # Find common elements (duplicates) among all three sets
    return sorted(list(duplicates))                                    # Convert set of duplicates to a sorted list


list1 = list(input("Enter elements for list1: ").split())             # Read input from the user for three lists
list2 = list(input("Enter elements for list2: ").split())
list3 = list(input("Enter elements for list3: ").split())

print("Duplicate items:", duplicate_char(list1, list2, list3))         # function call to find and print duplicate items
