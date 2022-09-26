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
