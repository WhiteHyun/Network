from socket import *
if __name__ == "__main__":
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("", server_port))
    server_socket.listen(1)
    print("The server is ready to receive")
    sentence = ''
    while True:
        connection_socket, addr = server_socket.accept()
        while sentence != '':

            sentence = connection_socket.recv(1024).decode()
            capitalized_sentence = sentence.upper()
            print(f"Received from ({addr}), Message: '{sentence}'")
            connection_socket.send(capitalized_sentence.encode())
        connection_socket.close()
