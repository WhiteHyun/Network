import operator as op
from functools import reduce


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


# 패킷교환망 이항분포 계산 알고리즘
if __name__ == "__main__":
    user_percentage = int(input("유저가 active 되는 전체시간의 퍼센트(%): ")) / 100
    user_speed = float(input("유저 전송속도(kb/s): "))
    link_speed = float(input("링크 전송속도(Mbps): "))
    miman = float(input("회선 교환에 비해 지연(%) 미만 설계?: "))/100
    circuit_switching_user = int((link_speed*1000) // user_speed)
    n = circuit_switching_user+1
    i = 0
    while True:
        p = 0
        for r in range(circuit_switching_user+1):
            p += nCr(n, r)*((circuit_switching_user/100) ** r) * \
                ((1-circuit_switching_user/100)**(n-r))
        p = 1 - p
        if p >= miman:
            n -= 1
            break
        n += 1
    print("===================\n")
    print(f"회선교환방식 사용자수: {circuit_switching_user}")
    print(f"최대 사용자: {n}명")
    print(f"패킷교환망은 회선교환망에 비해 용량이 {n/circuit_switching_user}배 이상임")
