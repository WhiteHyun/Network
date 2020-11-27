import sys
from socket import *
from threading import Thread
from HttpRequest import httpReq

server_socket = socket(AF_INET, SOCK_STREAM)

server_port = 12000
thread_num = 1
access_address = []


server_socket.bind(("", server_port))
server_socket.listen(1)

with open("subnet_network_list.txt") as file:
    lines = file.readlines()
    for line in lines:
        access_address.append(line[:-1])
file.close()
print(f"accessible Sub-network: {access_address}")


while True:
    print('The server is ready to receive')
    connection_socket, addr = server_socket.accept()
    print(f"sender subnet address = {addr[0][:-2]}, host: {addr[0][-1]}")
    if not addr[0] in access_address:
        print(f"Access Failed, IP=({addr[0]})")
        continue

    th = Thread(target=httpReq, args=(connection_socket, thread_num))
    print(f"\nThread {thread_num} started\n")
    th.start()
    thread_num = thread_num+1


server_socket.close()
sys.exit()
