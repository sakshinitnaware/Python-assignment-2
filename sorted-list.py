def find_min_ele(sorted_list):                         # Define a function named find_min_ele that takes one parameter sorted_list
  if not sorted_list:                                  # Check if sorted_list is empty using the not operator and return None if it is
        return None
    
    return sorted_list[0]                             # Return the first element of sorted_list (which is assumed to be the minimum since the list is sorted)


sorted_list = [1, 2, 3, 4, 5]                        # Example list
print(find_min_ele(sorted_list))                     # find_min_ele function call with sorted_list as argument and print the result
