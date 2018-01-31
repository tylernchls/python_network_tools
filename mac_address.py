# Returns information on mac address entered

import urllib2
import json
import codecs

def mac_address_scan():

    url = 'http://macvendors.co/api/'
    mac_address = raw_input('Enter MAC Address To Search: ')

    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
    response = urllib2.urlopen(request)

    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

    print '=' * 40
    print (obj['result']['company'])
    print (obj['result']['address'])
    print '=' * 40

if __name__ == '__main__':
    mac_address_scan()
