# opens a file for reading
file = open('devices-01.txt', 'r')

# Reads the file one line ar a time and removes whitespace
name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()

# Display the device information
print('Device name: ', name)
print('IP address: ', ip_address)
print('OS type: ', os_type)
print('Username: ', username)
print('Password: ', password)

# Display the information using string formatting
print('--- Device information---')
print('')
print('Name IP address OS Username Password')
print('----- --------------- ----- -------- --------')
print('{0:8} {1:15} {2:8} {3:10} {4:10}'.format(name, ip_address,
 os_type, username,
 password))
print('')
print('----------------------------------------------------------------')

# Create comma-separated string of device information attributes
device_info = name # Device name
device_info = device_info + ',' + ip_address # add comma and IP address
device_info = device_info + ',' + os_type # add comma and os-type
device_info = device_info + ',' + username # add comma and username
device_info = device_info + ',' + password # add comma and password

#output
print('')
print('--- Writing device information to file --------------------------')
print('')
outfile = open('devices-01-out.csv', 'w') # open the output file
outfile.write(device_info) # write the line of device information
outfile.write('\n') # with 'write' we must add ending newline char
outfile.close() # close file when writing is complete
print('--- Device information written to file --------------------------')
print('')

# Opens the file made above
infile = open('devices-01-out.csv', 'r') # open the new one-line file
device_info = infile.readline().strip() # read the line from the file
infile.close() # close the file

# Displays the information from the file that was just created
print('')
print('--- Device info read from file ------------------------')
print('')
print('Device Info: ', device_info)
print('')
print('----------------------------------------------------------------')
print('')
