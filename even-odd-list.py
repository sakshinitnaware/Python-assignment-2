list_sample = [10, 501, 22, 37, 100, 87, 351] # list of numbers
even = []                                     # initialing vairiable for even list
odd = []                                      # initialing vairiable for odd list

for num in list_sample :                      # fro loop to ittrate over the num in list
    if num % 2 == 0 :                         # if else condition to ittrate over the even num in list with the condition of modulus 
        even.append(num)
    else :
        odd.append(num)
print(even)                                   # printing even and odd list seperately
print(odd)                                     
