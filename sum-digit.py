def sum_number(number):                                    # Define a function named sum_number that takes one parameter named number
    digit_sum = sum(int(digit) for digit in str(number))   # Convert the number to a string, iterate over each digit, convert it back to an integer,and calculate the sum of all digits using the sum() function.
    print(digit_sum)                                       # Print the calculated sum of digits to the console

number = int(input())                                      # Read an integer input from the user using input()

sum_number(number)                                         # Call the sum_number function and pass the input number as an argument
