from socket import *

IP_ADD = 0  # 클라이언트 주소의 주소와 포트 중 주소 인덱스를 가리킴

if __name__ == "__main__":
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("", server_port))
    server_socket.listen(1)
    print("The server is ready to receive")
    while True:
        sentence = ' '
        connection_socket, addr = server_socket.accept()
        while sentence != '':
            sentence = connection_socket.recv(1024).decode()
            capitalized_sentence = sentence.upper()
            print(f"Received from ({addr[IP_ADD]}), Message: '{sentence}'")
            connection_socket.send(capitalized_sentence.encode())
        connection_socket.close()
    server_socket.close()
