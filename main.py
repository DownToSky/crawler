sock = sock.socket()
sock.setblocking(Flase)
try:
    soc.connect(('xkcd.com',80))
except BlockingIOError:
    pass
    
request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
encoded = request.encode('ascii')

while True:
    try:
        soc.sent(encoded)
        break
    except OSError as e:
        pass

print('sent')