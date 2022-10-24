#Importing Assets
import pexpect
    # ^ Used for SSH and Telnet
import telnetlib
import getpass
    # ^ used for Saving Config File

#Assinging Variables
ip_address = '192.168.56.101'
#User Credentials
tel_username = 'cisco'
password = 'cisco123!'
ssh_username = 'prne'
#Admin password 
admin_password = 'class123!'

#-------------Telnet----------------#
def telnet_connect():
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
    print('Testing Username')
    session.sendline(tel_username)
    result = session.expect(['Password:', pexpect.TIMEOUT])

    if result != 0:
        print('Failure | Incorrect Username: ', tel_username)
        exit()

    #Password & Error Check
    print('Testing Password')
    session.sendline(password)
    #expect '#' as we should be logged into privilleged mode using a level 15 account
    result = session.expect(['#', pexpect.TIMEOUT])

    if result != 0:
        print('Failure | Incorrect Password: ', password)
        exit()
          
    # Final Message to allow user to see successful login
    print('-------------------------Telnet-----------------------------')
    print('> Connected to: ', ip_address)
    print('> Credentials <')
    print('> Username: ', tel_username)
    print('> Password: ', password) 
    print('------------------------------------------------------------')

    #End session
    #sends quit to console logging us out & informing user
    print('Quitting Telnet Connection. Goodbye', tel_username)
    session.sendline('quit')
    session.close()
    print('Disconnected.')
    
#-------------SSH----------------# 
def ssh_connect():
    #Let user know we're starting SSH Session  
    print('Begining SSH connection to ', ip_address)

    #Begin Session giving the user and IP encoded
    session = pexpect.spawn('ssh ' + ssh_username + '@' + ip_address,
     encoding='utf-8', timeout=20)
    result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

    #Error Check to allow user to know where issues lay
    if result != 0: 
        print( 'Failure to acquire: ', ip_address)
        print( 'Please check IP Address and Username then try again.')
        exit()

    #Password & Error Check
    session.sendline(password)
    #expect > as we should be logged into non-privilleged mode
    result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

    if result != 0:
        print('--- Failure | Incorrect Password: ', password)
        exit()
         
    # Message to confirm Logon
    print('-------------------------SSH-----------------------------')
    print('> Connected to: ', ip_address)
    print('> Credentials <')
    print('> Username: ', ssh_username)
    print('> Password: ', password) 
    print('---------------------------------------------------------')

    # Close SSH session
    session.close()
    print('Disconnected.')
    
#-------------Cisco Backup----------------# 
def configuration_backup():
    print('Begining Config Backup via Telnet')

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
    print('Testing Username')
    session.sendline(tel_username)
    result = session.expect(['Password:', pexpect.TIMEOUT])

    if result != 0:
        print('Failure | Incorrect Username: ', tel_username)
        exit()

    #Password & Error Check
    print('Testing Password')
    session.sendline(password)
    #expect '#' as we should be logged into privilleged mode using a level 15 account
    result = session.expect(['#', pexpect.TIMEOUT])

    if result != 0:
        print('Failure | Incorrect Password: ', password)
        exit()
    
    #Starts Telnetlib section  - If needed a for loop can be used to read multiple IPs from file  
    HOST = ip_address    
    tn = telnetlib.Telnet(HOST)
    #Commands to enter on cosole to get config
    #Suggested fix for sticking issues~~~~~~~~~~
    tn.read_until(b'Username: ')
    tn.write(tel_username.encode('ascii') + b'\n')
    if password:
        tn.write(password.encode('ascii') + b'\n')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tn.write(b'enable\n')
    tn.write(b'show run\n')
    #print("Running Config")
    tn.write(b'exit\n')
    
    #Output
    reading_control = tn.read_all()
    #make file in write mode
    save_control = open('Router_Config_' + HOST + '.txt', 'w')
    #Add decode here
    save_control.write(reading_control.decode('ascii'))
    save_control.write('\n')
    save_control.close()
    print(reading_control)
    
    # Final Message to allow user to see successful & What was done
    print('-------------------------Telnet-----------------------------')
    print('> Connected to: ', ip_address)
    print('> Credentials <')
    print('> Username: ', tel_username)
    print('> Password: ', password) 
    print('------------------------------------------------------------')

    #End session
    #sends quit to console logging us out & informing user
    print('Quitting Telnet Connection. Goodbye', tel_username)
    session.sendline('quit')
    session.close()
    print('Disconnected.')
    
#Execution - Add a menu 
print('Please Select what code you wish to run.')
print('1: Telnet Connection')
print('2: SSH Connection')
print('3: Configuration Backup - Telnet')

selection = input('Enter Number Here: ')
if selection == '1':
    telnet_connect()
elif selection == '2':
    ssh_connect()
elif selection == '3':
    configuration_backup()
else:
    print('Invalid Number, Try again.')
