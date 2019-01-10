import socket


IP = '192.168.2.4'  # IP referee box
PORT = 28097  # PORT komunikasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP, PORT)
sock.connect(server_address)
while True:
    #print(sys.stderr, '\nwaiting to receive message')
    # data, address = sock.recvfrom(4096)
    data = sock.recv(PORT)

    #print(sys.stderr, 'received %s bytes from %s' % (len(data), address))
    print(data.decode())

    '''if data:
        sent = sock.sendto(data, address)
        print(sys.stderr, 'sent %s bytes back to %s' % (sent, address))'''
