from socket import *
import time

if __name__ == "__main__":
    server_name = '10.101.3.27'  # Desktop 내부주소 언제든 변경 가능
    # server_name = '127.0.0.1'  # Desktop 내부주소 언제든 변경 가능
    server_port = 12000
    data_length = 1000  # 데이터 길이 많은 데이터를 보내고 싶을 경우 이를 수정하면 됨
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))  # 3-way handshake
    client_socket.settimeout(0.3)  # Read timeout
    count_error = 0  # 손실 횟수

    # 왕복시간을 구해 최소, 최대, 시간합을 구하기 위해 선언
    min_time = 100000
    max_time = sum_time = 0

    for data in range(1, data_length+1):
        data = f"ping{data} {time.asctime()}"
        # data = str(data)

        try:
            start = time.time()  # Sent time
            # Send the TCP packet with the ping message
            client_socket.send(data.encode())
            # Received the server response
            modified_message = client_socket.recv(1024)
            end = time.time()  # Received time

            # Round trip time is the difference between sent and received time
            round_trip_time = (end-start)*1000
            if round_trip_time > max_time:
                max_time = round_trip_time
            if round_trip_time < min_time:
                min_time = round_trip_time
            sum_time += round_trip_time

            print(
                f"{server_name}의 응답: Message='{modified_message.decode()}' 시간={int(round_trip_time)}ms")
        except IOError:
            # Server does not response
            # Assume the packet is lost
            print(f"Error! time out.")
            count_error += 1
            continue

    # Close the client socket
    client_socket.close()

    count_send = data_length  # 보낸 횟수
    count_recv = data_length - count_error  # 받은 횟수

    # ICMP 프로토콜 출력양식을 참고함
    print(f"""
    {server_name}에 대한 Ping 통계:
        패킷: 보냄 = {count_send}, 받음 = {count_recv}, 손실 = {count_error} ({count_error/count_send*100}% 손실)
    """)
    if count_recv != 0:
        print(f"""
    왕복 시간(밀리초):
        최소 = {int(min_time)}ms, 최대 = {int(max_time)}ms, 평균 = {int(sum_time // count_recv)}ms
    """)
