# Import Assets
import pexpect

#Variable List
ip_address = '192.168.56.101'
username = 'prne'
password = 'cisco123!'
password_enable = 'class123!'

# Open SSH Session giving username and IP to connect
session = pexpect.spawn('ssh ' + username + '@' + ip_address,
 encoding='utf-8', timeout=20)
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
# Error check
if result != 0:
 print('--- Failure | creating session for: ', ip_address)
 exit()
  
#Password and error check
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
 print('--- Failure | Incorrect Password: ', password)
 exit()
  
# Message to confirm Logon
print('--- Success! connecting to: ', ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
  
# Enter Privilleged mode /w Error checking
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
 print('--- Failure | Unable to eneter Privilleged Mode')
 exit()
  
# Admin Password
session.sendline(password_enable)
result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
 print('--- Failure | Retry password')
 exit()
  
# config mode
session.sendline('configure terminal')
result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
 print('--- Failure | Unable to enter config mode')
 exit()
  
# Insert what needs doing here an example is changing host name via
session.sendline('hostname R1')
result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])

if result != 0:
 print('--- Failure! setting hostname')
# Though more config can be done this way so long as you understand how

# Exit config mode
session.sendline('exit')
# Exit enable mode
session.sendline('exit')

# Completion Message - Change depending on task at hand
print('--- Success in task: Configuring Hostname) 

# Terminate SSH session
session.close()
