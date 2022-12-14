import netmiko

#Table to hold connect information
def loopback():
    connectionInfo = {
        "device_type":"cisco_ios", 
        "host":"192.168.56.101", #IP
        "username":"cisco",
        "password":"cisco",
        #Admin password
        "secret":"class", 
        }
        
    session = netmiko.ConnectHandler(**connectionInfo) # gives var session the netmiko child on the device
    session.enable() # Enables the config on router
    print('---- Connection Established | Loopback  ----')

    ##Example of command to insert
    #runConf = session.send_command("show running-config")

    #IP - enable > interface > ip address (ip) (subnet)
    #Loopback - enable > configure terminal > interface loopback 0 > Assign IP and Subnet > Exit
    #The IPv4 address for each loopback interface must be unique and unused by any other interface.
    #Return IP address via "show IP interface brief" 
    #Return loopback via "show ip command"
    
    config_commands = {
    
    'int loopback 1',
    'ip add 10.0.0.1 255.255.255.0',
    }
    
    #Uses table above to push commands.
    loopback_cmd = session.send_config_set(config_commands)
    print('---- Loopback Established ----')
    print('{}\n'.format (loopback_cmd))
    
    #Output
    ip_table = session.send_command('show ip interface brief')
    print('{}\n'.format (ip_table))
    

def menu():
  print('Please Select what code you wish to run.')
  print('1: Loopback Configuration')
  print('2: N/A')
  print('3: Exit')

  selection = input('Enter Selection Here: ')
  if selection == '1':
      loopback()
  elif selection == '2':
      print('WIP')
  elif selection == '3':
      print('Goodbye')
  else:
      print('Invalid Input, Try again.')

#Do not edit - Start 
if __name__ == '__main__':
    menu()
