import sys, time, threading
from socket import *
from datetime import datetime

target = ''

# Set port range below for scan
max_port = 100
min_port = 1
start_time = datetime.now()

def get_remote_ip(target):
    print ("-" * 60)
    print ("Please wait, determining ip address of: ", target)
    print ("-" * 60)
    time.sleep(3)

    print ("-" * 60)
    print ('Finished, ip address of target is: ', gethostbyname(target))
    print ("-" * 60)
    time.sleep(3)

def start_scan_time():
    print ("-" * 80)
    print ('Starting port scan on: %s current time: %s' %  (target,start_time))
    print ("-" * 80)
    time.sleep(3)


def scan_remote_host(target, port):
    try:
        # Creates new ipv4 socket, using tcp connection
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.5)
        response = s.connect_ex((target, port))

        if response == 0:
            print ('Port %d: Open' % port)
        s.close()

    except:
        pass

def main():

    target = input('Enter remote target: ')

    try:
        get_remote_ip(target)

        start_scan_time()

    except KeyboardInterrupt:
        print (' You pressed Ctrl+C. Shutting down program')
        sys.exit(1)

    for port in range(min_port, max_port):
        try:
            response = scan_remote_host(target, port)

            # Implements threading but not working correctly yet
            # thread = threading.Thread(target=scan_remote_host, args=(target, int(port)))
            # thread.start()

        except Exception as e:
            pass

    stop_time = datetime.now()
    total_time = stop_time - start_time
    print ('Scanning duration: %s...' % total_time)

if __name__ == "__main__":
    main()
