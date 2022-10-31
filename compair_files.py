#Import required assests
import re #used in ip_expression


#Build menu for user interaction & future use
def menu():
    #menu print
    print('~Inspecting Files for difference~')
    print('1: Running Config vs Start Up')
    print('2: Running Config vs Offline Backup')
    print('3: Version Check')
    print('4: Management IP Check')
    userinput = input('Select Option from list: ')
    #Menu spawns def after selection
    if userinput == '1':
        vs_startup()
    elif userinput == '2':
        vs_offline()
    elif userinput == '3':
        version_comapir()
    elif userinput == '4':
        ip_expression()
    else
        print('Invalid Input, Try Again')
def version_comapir():
    #Set current version value
    current_version = 'Version 5.3.1'
    
    # Read lines from file
    file = open('devices-06.txt', 'r')
    for line in file:
    
    #Place into list
    version_list = line.strip().split(',')
    
    #Place into dictionary
    device_information = {} # {} makes dictionary to be segmented
    device_information['name'] = version_list[0]
    device_information['ip'] = version_list[2]
    device_information['version'] = version_list[3]
    
    #Display message if version missmatch
    if device_information['version'] != current_version:
        print('Device:', device_information['name'],'   Version:', device_information['version'])
        print('')
    
    #Close file
    file.close

def ip_expression():
    # Create regular expression to find the Mgmt IP address
    re_ip_expression = re.compile(r'Mgmt:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    # Read lines from file
    file = open('devices-06.txt', 'r')
    for line in file:
    
    #Place into list
    version_list = line.strip().split(',')
    
    device_information = {} 
    device_information['name'] = device_info_list[0]

    #Get management ip and add to list
    management_ip = re_ip_expression.search(line)
    device_info['ip'] = management_ip.group(1)
    
    # Display device and management IP address
    print(' Device:', device_information['name'],' Management IP:', device_information['ip'])
    print('')
    
    #close
    file.close
def vs_startup
    print('wip')

def vs_offline():
    print('wip')

menu()
