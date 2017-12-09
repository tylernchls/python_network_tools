import urllib2

def client_request():
    try:
        user_input = raw_input('Enter url || ex. google.com: ')
        parse_input = 'http://www.' + user_input
        request = urllib2.urlopen(parse_input)
        response = request.read()

        print '=' * 20
        print 'The Url is: \n', request.geturl()
        print '=' * 20

        print '=' * 20
        print 'Status Code: \n', request.getcode()
        print '=' * 20

        print '=' * 40
        print 'Request Header Info: \n', request.info()
        print '=' * 40

        print '=' * 20
        print 'Server Info: \n', request.info()['server']
        print '=' * 20

        print '=' * 80
        print 'Site Data: \n', response
        print 'Length: ', len(response)
        print '=' * 80

        
    except urllib2.HTTPError, e:
        code = e.code
        print 'code', code

if __name__ == '__main__':
    client_request()
