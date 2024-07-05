# Function to calculate the sum of first and last digits of a number
def sum_first_last_digits(number):              # Convert number to string to easily access digits
    
    num_str = str(number)
    first_digit = int(num_str[0])              # Get the first digit (converted back to integer)
    last_digit = int(num_str[-1])              # Get the last digit (converted back to integer)
    sum_digits = first_digit + last_digit      # Calculate the sum of first and last digits
    return sum_digits                          # Return the sum of first and last digits

user_input = int(input("Enter a number: "))    # Read an integer input from the user
result = sum_first_last_digits(user_input)     # Call the function to calculate the sum of first and last digits
print("Sum of first and last digits:", result) # Print the result
