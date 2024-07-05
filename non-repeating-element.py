def find_non_repeating_element(nums):                     # Initialize an empty dictionary to store counts of each element
    count_dict = {}                                       # Count occurrences of each element in the list
    for num in nums:
        if num in count_dict:               
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
   
    for num in nums:                                   # Find the element with count equal to 1 (non-repeating)
        if count_dict[num] == 1:
            return num
    
    
    return None                                       # Return None if no non-repeating element is foundn


nums = [1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8]             # sample input
result = find_non_repeating_element(nums)
print("Non-repeating element:", result)
