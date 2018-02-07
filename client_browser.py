import urllib.request

def client_request():
    user_input = input('Enter url || ex. google.com: ')
    parse_input = 'http://www.' + user_input
    user_request = urllib.request.urlopen(parse_input)
    response = user_request.read()

    print ('=' * 20)
    print ('The Url is: \n', user_request.geturl())
    print ('=' * 20)

    print ('=' * 20)
    print ('Status Code: \n', user_request.getcode())
    print ('=' * 20)

    print ('=' * 80)
    print ('Response Header Info: \n', user_request.info())
    print ('=' * 80)

    print ('=' * 20)
    print ('Server Info: \n', user_request.info()['server'])
    print ('=' * 20)

    print ('=' * 80)
    print ('Site Data: \n', response)
    print ('Length: ', len(response))
    print ('=' * 80)

if __name__ == '__main__':
    client_request()

