#A3 - Do one of the following (Do more if confident) 

#Loopback & IP Address
#A Protocol from the list - OSPF/EIGRP/RIP
#Simultanious or Sequence config of two network devices with VLAN configs deployed 

#Import List - Libaries used to make the program function
import netmiko


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

    ##Example of command to insert
    #runConf = session.send_command("show running-config")

def loopback_commands
    #IP - enable > interface > ip address (ip) (subnet)
    #Loopback - enable > configure terminal > interface loopback 0 > Assign IP and Subnet > Exit
    #The IPv4 address for each loopback interface must be unique and unused by any other interface.
    #Return IP address via "show IP interface brief" 
    #Return loopback via "show ip command"
    
    
def loopback
    connect()
    loopback_commands()
    
def menu():
    menu = []
    print('WIP')
