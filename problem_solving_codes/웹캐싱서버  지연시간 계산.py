if __name__ == "__main__":
    size = int(input("객체 크기(k-bit): "))
    request = int(input("기점 서버 평균 요청 비율(/sec): "))
    internet_trip_time = (int(input("인터넷 라우터 요청으로부터 기점서버 응답시간(인터넷지연)(sec): ")))
    access_link = int(input("액세스 링크(kbps): "))
    LAN_speed = int(input("기업체 간 LAN 전송률(kbps): "))
    gotcha = float(input("적중률(%): "))/100

    access_trip_time = request*size/access_link  # 트래픽강도
    LAN_trip_time = request*size/LAN_speed  # LAN 지연
    print("\n===========웹 캐싱 사용 X===========\n")
    print(f"액세스링크 트래픽강도: {access_trip_time}")
    print(
        f"전체지연 = 인터넷지연 + 액세스지연 + LAN 지연 = {internet_trip_time} + {'infinite' if access_trip_time == 1.0 else access_trip_time} + {LAN_trip_time}")
    print()
    cashing_access_trip_time = request*size*(1-gotcha)/access_link
    print("\n===========웹 캐싱 사용 O===========\n")
    print(f"액세스링크 트래픽강도: {cashing_access_trip_time}")
    print(
        f"전체지연 = {1-gotcha}*(기점서버로부터 지연) + {gotcha}*(캐시에 의한 랜지연) = {1-gotcha}({internet_trip_time}초+{size/access_link:.3f}+{size/LAN_speed}) + {gotcha}({size/LAN_speed})")
    print(f"={(1-gotcha)*(internet_trip_time+size/access_link+size/LAN_speed)+(gotcha)*(size/LAN_speed):.3f}")
    print()
