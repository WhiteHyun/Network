from socket import *
from time import sleep


def httpReq(conn_socket, thread_num):
    try:
        # Receives the request message from the client
        message = conn_socket.recv(2048).decode()
        print(message)

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        file_name = message.split()[1]
        print(file_name)

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        myfile = open(file_name[1:], "rb")

        # Store the entire contenet of the requested file in a temporary buffer
        response = myfile.read()
        myfile.close()

        # Send the HTTP response header line to the connection socket
        header = 'HTTP/1.1 200 OK\n'

        if file_name.endswith(".jpg"):
            file_type = "image/jpg"
        elif file_name.endswith(".gif"):
            file_type = "image/gif"
        elif file_name.endswith(".mp4"):
            file_type = "video/mp4"
        elif file_name.endswith(".wmv"):
            file_type = "video/wmv"
        elif file_name.endswith(".html"):
            file_type = "text/html"
        else:
            raise IOError

        header += f"Content-Type: {str(file_type)}\n\n"
        print(header)

        # Send the content of the requested file to the connection socket
        conn_socket.send(header.encode())
        conn_socket.send(response)
        # Close the client connection socket
        conn_socket.close()

        for i in range(1, 10):
            sleep(1)
            print(f"thread number: {thread_num}, sleep count: {i}")

    except IOError:
        # Send HTTP response message for file not found
        header = "HTTP/1.1 404 Not Found\n\n"
        response = "<html><head></head><body><h1>Error 404: File not found</h1><p>Python HTTP Server</p></body></html>".encode()

        print(header)
        conn_socket.send(header.encode())
        conn_socket.send(response)
        # Close the client connection socket
        conn_socket.close()
