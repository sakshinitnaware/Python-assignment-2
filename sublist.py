def has_zero_sum_sublist(arr):                               # Define a function named has_zero_sum_sublist that takes one parameter arr
    seen_sums = set()                                        # Initialize an empty set to keep track of seen sums
    current_sum = 0                                          # Initialize a variable to keep track of the current sum
    for num in arr:                                          # Iterate through each element num in the input array arr
        current_sum += num                                   # Update the current sum by adding the current element num
        if current_sum == 0 or current_sum in seen_sums:     # Check if the current sum is zero or if it has been seen before in seen_sums
            return True
        seen_sums.add(current_sum)                            # Add the current sum to seen_sums
    return False                                               # If no zero-sum sublist is found, return False

arr = [4, 2, -3, 1, 6]                                      # sample arr
print(has_zero_sum_sublist(arr))
