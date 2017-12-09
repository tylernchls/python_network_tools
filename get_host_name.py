#USES PYTHON 2.7

#SCRIPT TO GET MACHINE NAME
import socket
def print_machine_info():
    host_name = socket.gethostname()
    print 'The hostname is: ', host_name
    
if __name__ == '__main__':
    print_machine_info()
