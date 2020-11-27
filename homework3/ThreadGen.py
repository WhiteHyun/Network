import sys  # In order to terminate the program
from socket import *  # Import socket module
from threading import Thread
from HttpRequest import httpReq


# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
server_socket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
server_port = 12000
thread_num = 1


# Bind the socket to server address and server port
server_socket.bind(("", server_port))

# Listen to at most 1 connection at a time
server_socket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
    print('The server is ready to receive')

    # Set up a new connection from the client
    connection_socket, addr = server_socket.accept()
    th = Thread(target=httpReq, args=(connection_socket, thread_num))
    print(f"\nThread {thread_num} started\n")
    th.start()
    thread_num = thread_num+1


server_socket.close()
sys.exit()
