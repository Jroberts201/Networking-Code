#A3 - Do one of the following (Do more if confident) 

#Loopback & IP Address
#A Protocol from the list - OSPF/EIGRP/RIP
#Simultanious or Sequence config of two network devices with VLAN configs deployed 

#Import List - Libaries used to make the program function
import netmiko

#Table to hold connect information
def connect():
    connectionInfo = {
        "device_type":"cisco_ios", 
        "host":"", #IP
        "username":"cisco",
        "password":"cisco", 
        "secret":"class" #Admin password
        }
        
    session = netmiko.ConnectHandler(**connectionInfo) # gives var session the netmiko child on the device
    session.enable() # Enables the config on router
    print('---- Connection Established ----')

    ##Example of command to insert
    #runConf = session.send_command("show running-config")

def loopback_commands
    #IP - enable > interface > ip address (ip) (subnet)
    #Loopback - enable > configure terminal > interface loopback 0 > Assign IP and Subnet > Exit
    #The IPv4 address for each loopback interface must be unique and unused by any other interface.
    #Return IP address via "show IP interface brief" 
    #Return loopback via "show ip command"
    config_commands = {
    'config terminal',
    'int loopback 1',
    'ip add 10.0.0.1 255.255.255.0',
    }
    
    #Uses table above to push commands.
    loopback_cmd = session.connectionInfo.send_config_set()config_commands
    print('---- Loopback Established ----')
    print('{}\n'.format (loopback_cmd))
    
    #Output
    ip_table = session.connectionInfo.send_command('show ip interface brief')
    print('{}\n'.format (ip_table))
    
def loopback_execute
    connect()
    loopback_commands()
    
def menu():
  print('Please Select what code you wish to run.')
  print('1: Loopback Configuration')
  print('2: N/A')
  print('3: Exit')

  selection = input('Enter Selection Here: ')
  if selection == '1':
      loopback_execute()
  elif selection == '2':
      print('WIP')
  elif selection == '3':
      print('Goodbye')
  else:
      print('Invalid Input, Try again.')

#Do not edit - Start 
if __name__ == '__main__':
    menu()
