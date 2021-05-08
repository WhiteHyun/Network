from socket import *
import time

IP_ADD = 0  # 클라이언트 주소의 주소와 포트 중 주소 인덱스를 가리킴
if __name__ == "__main__":
    server_name = '10.101.3.27'  # Desktop 내부주소 언제든 변경 가능
    server_port = 12000
    data_length = 1000  # 데이터 길이 많은 데이터를 보내고 싶을 경우 이를 수정하면 됨
    server_address = 0  # 서버 주소 미리 선언(unbound를 피하기 위함)
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(1)  # 연결지연시간을 1초로 설정
    count_error = 0  # 손실 횟수

    # 왕복시간을 구해 최소, 최대, 시간합을 구하기 위해 선언
    min_time = 100000
    max_time = sum_time = 0

    for data in range(1, data_length+1):
        data = f"ping{data} {time.asctime()}"

        try:
            start = time.time()  # Sent time
            # Send the UDP packet with the ping message
            client_socket.sendto(data.encode(), (server_name, server_port))
            # Received the server response
            modified_message, server_address = client_socket.recvfrom(2048)
            end = time.time()  # Received time

            # Round trip time is the difference between sent and received time
            round_trip_time = (end-start)*1000
            if round_trip_time > max_time:
                max_time = round_trip_time
            if round_trip_time < min_time:
                min_time = round_trip_time
            sum_time += round_trip_time

            print(
                f"{server_address[IP_ADD]}의 응답: Message='{modified_message.decode()}' 시간={round_trip_time:.2f}ms")
        except IOError:
            # Server does not response
            # Assume the packet is lost
            print(f"Error! time out.")
            count_error += 1
            continue

    count_send = data_length  # 보낸 횟수
    count_recv = data_length - count_error  # 받은 횟수

    # ICMP 프로토콜 출력양식을 참고
    print(f"""
    {server_address[IP_ADD]}에 대한 Ping 통계:
        패킷: 보냄 = {count_send}, 받음 = {count_recv}, 손실 = {count_error} ({count_error/count_send*100}% 손실)
    왕복 시간(밀리초):
        최소 = {int(min_time)}ms, 최대 = {int(max_time)}ms, 평균 = {int(sum_time // count_recv)}ms
    """)

    # Close the client socket
    client_socket.close()
