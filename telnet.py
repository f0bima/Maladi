import socket
IP = '192.168.2.4'  # IP referee box
PORT = 28097  # PORT komunikasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conect ke referee box
sock.connect((IP, PORT))
while 1:
    receive = sock.recv(PORT)
    print(receive.decode())  # penerimaan data
