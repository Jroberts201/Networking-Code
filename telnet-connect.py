#Importing Assets
import pexpect

#Assinging Variables
ip_address = '192.168.56.101'
#User Credentials
tel_username = 'cisco'
tel_password = 'cisco123!'
ssh_username = ''
ssh_password = ''
#Admin password 
admin_password = ''

#-------------Telnet----------------#

#Informing User of startup and warning of security risk
print('Begining Telnet connection to ', ip_address, ' Please note this is not Secure.')
#Create Telnet session - Spawn Session with IP & Include a 20 second countdown to timeout
session = pexpect.spawn('telnet ' + ip_address, timeout=20)
#Expect username if not Timeout
result = session.expect(['Username:', pexpect.TIMEOUT])

#Error Check to allow user to know where issues lay
if result != 0: 
    print( 'Failure to acquire: ', ip_address)
    print( 'Please check IP Address and try again.')
    exit()
print('Connected to ', ip_address)
#Credentials now must be sent
#Username & Error Check
session.sendline(tel_username)
result = session.expect(['Password:', pexpect.TIMEOUT])

if result != 0:
    print('Failure | Incorrect Username: ', tel_username)
    exit()

#Password & Error Check
session.sendline(tel_password)
#expect # as we should be logged into privilleged mode using a level 15 account
result = session.expect(['#', pexpect.TIMEOUT])

if result != 0:
    print('Failure | Incorrect Password: ', tel_password)
    exit()
      
# Final Message to allow user to see successful login
print('-------------------------Telnet-----------------------------')
print('> Connected to: ', ip_address)
print('> Credentials <')
print('> Username: ', tel_username)
print('> Password: ', tel_password) 
print('------------------------------------------------------------')

#End session
#sends quit to console logging us out & informing user
print('Quitting Telnet Connection. Goodbye', tel_username)
session.sendline('quit')
session.close()
