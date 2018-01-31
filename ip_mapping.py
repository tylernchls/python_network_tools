# Returns ip address of domain

import time
from socket import *

target = raw_input('Enter remote target: ')

def get_remote_ip(target):
    print "-" * 60
    print "Please wait, determining ip address of: ", target
    print "-" * 60
    time.sleep(3)

    print "-" * 60
    print 'Finished, ip address of target is: ', gethostbyname(target)
    print "-" * 60


if __name__ == "__main__":
    get_remote_ip(target)