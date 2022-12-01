#Connection and Command Handler
import netmiko

#Table to hold connect information
def loopback():
    connectionInfo = {
        'device_type':'cisco_ios', 
        'host':'192.168.56.101', #IP
        'username':'cisco',
        'password':'cisco',
        #Admin password
        'secret':'class', 
        }
 #Before running make sure you've set up username and password as it will error       
    session = netmiko.ConnectHandler(**connectionInfo) # gives var session the netmiko child on the device
    session.enable() # Enables the config on router
    print('---- Connection Established | Loopback  ----')

    ##Example of command to insert
    #runConf = session.send_command('show running-config')

    #IP - enable > interface > ip address (ip) (subnet)
    #Loopback - enable > configure terminal > interface loopback 0 > Assign IP and Subnet > Exit
    #The IPv4 address for each loopback interface must be unique and unused by any other interface.
    #Return IP address via 'show IP interface brief' 
    #Return loopback via 'show ip command'
    
    #Asks how many Loopbacks you want
    while True:
        try:
            runTime = int(input('Enter Loopback Count: '))
        except ValueError:
            print('Please, enter a valid number')
            continue
        else:
            print(f'You entered: {runTime}')
            break

        if runTime > '2048':
            print('You cannot make more then 2048 Loopback Addresses')
   
   
    
    #Sends cmds
    while runTime > 0: 
        #For some reason ip add is sometimes send before int loopback - Resolutions?
         #    - Fix - [] not {}
        config_commands = [
        f'int loopback {runTime}',     
        f'ip add 172.0.{runTime}.1 255.255.255.0',               
        ]

        #Uses table above to push commands enters conf t and ends automatically.
        loopback_cmd = session.send_config_set(config_commands)
        #Lets users know where we are in running
     
    

        print(f'---- Loopback {runTime} Established ----')
        #New line before Print
        print('{}\n'.format (loopback_cmd))

        #Reduces number by 1 to lower all inputs
        runTime = runTime - 1
        
    #Output
    ip_table = session.send_command('show ip interface brief')
    print('{}\n'.format (ip_table))
    #Disconnects from session
    session.disconnect()

def OSPF():
   print('Begining OSPF Config')
   print('Please be aware this command will create loopback interface 100 on 10/20.0.0.1')
  
   
   CSR = {
       'device_type':'cisco_ios', 
       'host':'192.168.56.101', #IP
       'username':'cisco',
       'password':'cisco',
       #Admin password
       'secret':'class', 
       }

   R2 = {
       'device_type':'cisco_ios', 
       'host':'192.168.56.130', 
       'username':'cisco',
       'password':'cisco',
       #Admin password
       'secret':'class', 
       }
#Before running make sure you've set up username and password as it will error   
# Use router list to config at the same time - Idea scrapped different codes needed
   #router_list = [CSR, R2]

   session_CSR = netmiko.ConnectHandler(**CSR)
   session_CSR.enable
   session_R2 = netmiko.ConnectHandler(**R2)
   session_R2.enable

   #for router in router_list():
         
   
   csr_commands = [
   'int loopback 100',     
   'ip add 10.0.0.1 255.0.0.0',               
   ]
   
   r2_commands = [
   'int loopback 100',     
   'ip add 20.0.0.1 255.0.0.0',               
   ]
   
   #Uses table above to push commands enters conf t and ends automatically.
   loopback_csr = session_CSR.send_config_set(csr_commands)        
   loopback_r2 = session_R2.send_config_set(r2_commands)
   

   print('---- Loopback Established ----')
   print('{}\n'.format (loopback_csr))
   print('{}\n'.format (loopback_r2))
   print('---- IP View ----')
   ip_csr = session_CSR.send_command('show ip interface brief')
   print('{}\n'.format (ip_csr))
   
   ip_r2 = session_R2.send_command('show ip interface brief')
   print('{}\n'.format (ip_r2))
   
   rip_csr = [
   'router rip'
   'network 172.16.1.0' 
   'network 10.0.0.0'    
   ]
   rip_r2 = [
   'router rip'
   'network 172.16.1.0'
   'network 20.0.0.0' 
   ]
   
   print('---- RIP Established ----')
   sh_rip_csr = session_CSR.send_command('show ip route rip')
   print('{}\n'.format (sh_rip_csr))
   
   sh_rip_r2 = session_R2.send_command('show ip route rip')
   print('{}\n'.format (sh_rip_r2))
        
   session_CSR.disconnect
   session_R2.disconnect
        
def menu():
  print('Please Select what code you wish to run.')
  print('1: Loopback Configuration')
  print('2: OSPF Configuration')
  print('3: Exit')

  selection = input('Enter Selection Here: ')
  if selection == '1':
      loopback()
  elif selection == '2':
      OSPF()
  elif selection == '3':
      print('Goodbye')
  else:
      print('Invalid Input, Try again.')

#Do not edit - Start 
if __name__ == '__main__':
    menu()
