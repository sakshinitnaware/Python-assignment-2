def happy_number(n):                                           # defining a function to perform the calculation 
    data = set()                                               # defining data as a set  
    while n != 1 and n not in data:                            # while loop to itterate until n is not 1 and not present in set 
        data.add(n)                                            # appending n in data
        n = sum(int(digit)**2 for digit in str(n))             # formula to calculate happy no.
    return n == 1                                              # returing if n is 1 and stop the loop

list_sample = [10, 501, 22, 37, 100, 999, 87, 351]              # sample list 
happy = []                                                      # defining the empty variable as list type  
nhappy = []                                                   

for num in list_sample:                                        # for loop to itterate over the num in list sample
    if happy_number(num):                                      # if else condition to append the happy number in happy list and nhappy list
        happy.append(num)
    else:
        nhappy.append(num)

print("Happy list:", happy)                                   # printing happy number and non happy numbers in a list
print("Non-happy list:", nhappy)
