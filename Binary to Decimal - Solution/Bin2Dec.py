binaryNumber = input("Type a binary number (any size): ") # recives a binary number as a string and stores at the variable 'binaryNumber'

value = 0 # This is the value that will be printed as the decimal number
times = 0 # This is the power that the 2 number will be raised

for number in binaryNumber[::-1]: # This for loop will get each 0 or 1 number
    if(number == ' '): 
        continue # Ignore's the charactere ' ' (blank space)
    value += int(number)*(2**(times)) # that number (1 or 0) will be multiplied by 2 eraised to the 'times' power and will be stored at the variable 'value' until the end of the string
    times += 1 # that way we can guarantee that the number will be raised to a different power each complete cicle of the for loop
    
print ("The binary number: {} corresponds to the decimal number: {}" .format(binaryNumber,value)) # That printed value will be the corresponding decimal number from that binary number recived
