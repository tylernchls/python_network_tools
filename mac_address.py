# Returns information on mac address entered
import urllib.request
import json
import codecs

def mac_address_scan():

    url = 'http://macvendors.co/api/'
    mac_address = input('Enter MAC Address To Search: ')

    payload = urllib.request.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
    print(payload)
    user_request = urllib.request.urlopen(payload)

    reader = codecs.getreader("utf-8")
    obj = json.load(reader(user_request))

    print ('=' * 40)
    print ((obj['result']['company']))
    print ((obj['result']['address']))
    print ('=' * 40)

if __name__ == '__main__':
    mac_address_scan()
