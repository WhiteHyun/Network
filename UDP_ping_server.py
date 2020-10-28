from socket import *
IP_ADD = 0  # 클라이언트 주소의 주소와 포트 중 주소 인덱스를 가리킴
if __name__ == "__main__":
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(("", server_port))

    print("The server is ready to receive")

    while True:
        message, client_address = server_socket.recvfrom(2048)
        modified_message = message.decode().upper()
        print(
            f"Received from ({client_address[IP_ADD]}), Message: '{message.decode()}'")
        server_socket.sendto(modified_message.encode(), client_address)
