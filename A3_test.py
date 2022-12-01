#Connection and Command Handler
import netmiko
#Time to ensure code is sent in appropriate order
import time
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
 #Before running make sure you've set up username and password as it will error       
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
    
    #Asks how many Loopbacks you want
   # while True:
   #     try:
   #         runTime = int(input("Enter how many Loopback Count: "))
   #     except ValueError:
   #         print("Please, enter a valid number")
   #         continue
   #     else:
   #         print(f'You entered: {runTime}')
   #         break

   #     if runTime > '2048':
   #         print('You cannot make more then 2048 Loopback Addresses')
   
    print('Sorry however for now only 1 loopback may be made for this time')
    runTime = 1
    #Sends 
    while runTime > 0: 
        #For some reason ip add is sometimes send before int loopback - Resolutions?
        #    - Remove this dict and use line.send to do it individually 
        #    - 
        
        config_commands = {
        f'int loopback {runTime}',
        #Why does adding another fix it? - Does not fix 100% maybe 2/3
        #f'int loopback {runTime}',
        
        f'ip add 172.0.{runTime}.1 255.255.255.0',
        
        
        }

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
