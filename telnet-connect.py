#Importing required assests
import pexpect

#Variable List
ip_address = '192.168.x.x'
username = 'cisco' #example name
password = 'cisco123!' #example password

#Open telenet
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8', timeout=20)
result = session.expect(['Username:', pexpect.TIMEOUT])

#Error check
if result != 0:
  print("Failure to create session: ", ip_address)
  exit()
  
#Sending Details

#Username + error catch
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

if result != 0:
  print("Failure | Incorrect Username: ", username)
  exit()
  
#Password + error catch
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

if result != 0:
  print("Failure | Incorrect Username: ", password)
  exit()
  
  # Success Message
print('--- Success! connecting to: ', ip_address)
print('--- Username: ', username)
print('--- Password: ', password)
print('------------------------------------------------------'
  
