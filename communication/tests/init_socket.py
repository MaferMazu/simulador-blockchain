from sys import argv, exit
from socket import socket
from threading import Thread
from multiprocessing import Process


def main(args):
    """Main function."""
    
    try:
        port = args[0]
        try:
            listen = args[1]
        except:
            listen = 10
        new_socket = socket()
        new_socket.bind(('localhost',port))
        new_socket.listen(listen)
        while True:
            connection, address = new_socket.accept()
            client = client + 1
            my_thread = Thread(target=receive_connection, connection=connection)
            my_thread.start()     
    except:
        pass


def receive_connection(connection):
    """Receive Connection"""

    while True:
        response = connection.recv(1024)
        if response:
            print(f">> Client {client}\n{response}")
        else:
            exit()
    connection.close()


if __name__=="__main__":
    main(argv[1:])