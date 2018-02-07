#USES PYTHON 2.7
# Retrieves hostname of client computer

import socket
def print_host_name():
    host_name = socket.gethostname()
    print ('The hostname is: ', host_name)

if __name__ == '__main__':
    print_host_name()
