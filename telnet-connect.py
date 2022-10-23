#Importing Assets
import pexpect

#Assinging Variables
#Get IP address from topology ASAP
ip_address = 'x.x.x.x'
#User Credentials
username = ''
password = ''
#Admin password 
admin_password = ''


#-------------Telnet----------------#
#Informing User of startup and warning of security risk
print('Begining Telnet connection to ', ip_address, ' Please note this is not Secure.')
#Create Telnet session - Spawn Session with IP & Include a 20 second countdown to timeout
session = pexpect.spawn('telnet ' + ip_address, timeout=20)
#Expect username if not Timeout
result = session.expect(['username:', pexpect.TIMEOUT])

#Error Check to allow user to know where issues lay
if result != 0: 
    print( 'Failure to acquire: ', ip_address)
    print( 'Please check IP Address and try again.')
    exit()
    
#Credentials now must be sent
#Username & Error Check
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

if result != 0:
    print('Failure | Incorrect Username: ', username)
    exit()

#Password & Error Check
session.sendline(password)
#expect > as we should not be logged into privilleged mode
result = session.expect(['>', pexpect.TIMEOUT])

if result != 0:
    print('Failure | Incorrect Password: ', password)
    exit()
      
# Final Message to allow user to see successful login
print('-------------------------Telnet-----------------------------')
print('> Connected to: ', ip_address)
print('> Credentials <')
print('> Username: ', username)
print('> Password: ', password) 
print('------------------------------------------------------------')

#End session
#sends quit to console logging us out & informing user
print('Quitting Telnet Connection. Goodbye', username)
session.sendline('quit')
session.close()
