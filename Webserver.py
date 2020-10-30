# Import socket module
from socket import *
import sys  # In order to terminate the program

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

server_socket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
server_port = 7777


# Bind the socket to server address and server port
server_socket.bind(("", server_port))

# Listen to at most 1 connection at a time
server_socket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
    print('The server is ready to receive')

    # Set up a new connection from the client
    conn_socket, addr = server_socket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = conn_socket.recv(2048).decode()
        print(message)

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        print(filename)

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        # rb = 'read, binary'
        myfile = open(filename[1:], "rb")

        # Store the entire contenet of the requested file in a temporary buffer
        response = myfile.read()
        myfile.close()
        # Send the HTTP response header line to the connection socket
        header = "HTTP/1.1 200 OK\n"

        if filename.endswith(".jpg"):
            filetype = "image/jpg"
        elif filename.endswith(".gif"):
            filetype = "image/gif"
        elif filename.endswith(".mp4"):
            filetype = "video/mp4"
        elif filename.endswith(".wmv"):
            filetype = "video/wmv"
        elif filename.endswith(".html"):
            filetype = "text/html"
        else:
            raise IOError

        header += f"Content-Type: {str(filetype)}\n\n"
        print(header)

        # Send the content of the requested file to the connection socket
        conn_socket.send(header.encode())
        conn_socket.send(response)
        # Close the client connection socket
        conn_socket.close()

    except IOError:
        # Send HTTP response message for file not found
        header = "HTTP/1.1 404 Not Found\n\n"
        response = "<html><head></head><body><h1>404 Not Found</h1></body></html>".encode()
        print(header)
        conn_socket.send(header.encode())
        conn_socket.send(response)
        # Close the client connection socket
        conn_socket.close()

server_socket.close()
sys.exit()  # Terminate the program after sending the corresponding data
