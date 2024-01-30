import socket

HOST ='#'
PORT =8081
server = socket.socket()
server.bind((HOST,PORT))
server.listen(1)
client, client_addr = server.accept()

while True:
    command = input('enter command: ')
    command = command.encode()
    client.send(command)
    output = client.recv(1024)
    output = output.decode()