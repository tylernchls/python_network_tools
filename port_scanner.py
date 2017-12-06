import sys, time, threading
from socket import *
from datetime import datetime

target = ''
max_port = 81
min_port = 70

# Retreives ip address of remote target
def get_remote_ip(target):
    print "-" * 60
    print "Please wait, determining ip address of: ", target
    print "-" * 60
    time.sleep(3)

    print "-" * 60
    print 'Finished, ip address of target is: ', gethostbyname(target)
    print "-" * 60
    time.sleep(3)

# Scans remote target based on host and port range by trying to make connection
def scan_remote_host(target, port):
    try:
        # Creates new ipv4 socket, using tcp connection
        s = socket(AF_INET, SOCK_STREAM)
        response = s.connect_ex((target, port))
        # If connect, print port then close socket
        if response == 0:
            print 'Port %d: Open' % port
        s.close()
    # Allows program to keep running if error occurs
    except:
        pass

def main():
    ######## Code starts here on run.
    try:
        target = raw_input('Enter remote target: ')

        # Calls function to get/display ip address of host
        get_remote_ip(target)

    # Basic error handling
    except Exception, e:
        print "Error: ", e
        sys.exit()

    # Starts timer for scan.
    start_time = datetime.now()
    print "-" * 80
    print 'Starting port scan on: %s, current time: %s' %  (target,start_time)
    print "-" * 80
    time.sleep(3)

    # Loops through port range
    for port in range(min_port, max_port):
        try:
            # Calls function and passes host & port
            response = scan_remote_host(target, port)

            ##### Enables threading but no increase in speed
            # thread = threading.Thread(target=scan_remote_host, args=(target, int(port)))
            # thread.start()

        # Allows program to keep running if error occurs
        except Exception, e:
            pass

    stop_time = datetime.now()
    total_time = stop_time - start_time
    print 'Scanning duration: %s...' % total_time

### Tells to execute main function
if __name__ == "__main__":
    main()
