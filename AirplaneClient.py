import socket
import time
import os


def connect_to_server():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    message = input('->')
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    s.close()

def main():
    pass

if __name__ == '__main__':
    main()


def connect_to_client():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    c, addr = s.accept()
    print("Connection was achieved. Connected from ", str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From Connected User: " + str(data))
        c.send(data.encode('utf-8'))
    c.close()