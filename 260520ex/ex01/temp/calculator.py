def add(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")


def sub(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")


def mul(n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")


def div(n1, n2):
    if n2 == 0:
        print("세상 어떤 숫자도 0으로 나눌 수는 없습니다.")
        return

    print(f"{n1} / {n2} = {n1 / n2}")


def rst(n1, n2):
    print(f"{n1} % {n2} = {n1 % n2}")


def prt(n1, n2):
    print(f"{n1} // {n2} = {n1 // n2}")
