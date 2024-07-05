list_sample = [10, 501, 22, 37, 100, 999, 87, 351]   # list of numbers
prime = []                                           # variable for prime list
non_prime = []                                       # variable for non-prime list

def is_prime(number):                                # funtion to perform prime and non-prime conditions
    if number < 2:                                   # if condition to see the num is less that 2 then its not prime 
        return False
    for i in range(2, int(number**0.5) + 1):         # for loop to check its factor from 2 to sq root 
        if number % i == 0:                          # if condition to check if no factors found then its prime 
            return False
    return True

for num in list_sample:                               # Iterate through each number in the list
    if is_prime(num):                                 # to heck if the number is prime using the is_prime function
        prime.append(num)
    else:
        non_prime.append(num)

print("Prime list:", prime)                           # printing Prime list and Non-prime list 
print("Non-prime list:", non_prime)
