# def setSensorActivate(state):
#     text = ""
#     if state:
#         text = "온도센서 작동을 시작합니다."
#     else:
#         text = "온도센서 작동을 중지합니다."

#     return text


# print(setSensorActivate(True))
# print(setSensorActivate(False))


# def toInch(length):
#     return float(length) / 2.54


# length = input("길이를 입력하세요(cm): ")
# print(f"{length}cm = {toInch(10):.2f}inch")


# def getDistance(time, speed):
#     return time * speed


# time = float(input("이동 시간 입력(h): "))
# speed = float(input("이동 속도 입력(km/h): "))

# print(f"이동 거리: {getDistance(time, speed)}km")


# def func1():
#     print("func1 Called")


# def func2():
#     print("func2 Called")


# def func3():
#     func1()
#     func2()
#     print("func3 Called")


# func3()


# def func4():
#     print("func4 called")
#     func4()


# func4()

# KOR = 1
# ENG = 2
# JPN = 3


# def printIntroText(option):
#     if option == KOR:
#         print("안녕하세요!")
#     elif option == JPN:
#         print("KONNICHIWA!")
#     else:
#         print("Howdy!")


# print(f"{KOR}.한국 {ENG}.미국 {JPN}.일본")
# selectedOpt = int(input("출신 국가: "))
# printIntroText(selectedOpt)


# def calc(num1, num2, operator):
#     match (operator):
#         case "+":
#             return add(num1, num2)
#         case "-":
#             return sub(num1, num2)
#         case "*":
#             return mul(num1, num2)
#         case _:
#             return div(num1, num2)


# def add(num1, num2):
#     return num1 + num2


# def sub(num1, num2):
#     return num1 - num2


# def mul(num1, num2):
#     return num1 * num2


# def div(num1, num2):
#     return num1 / num2


# inputs = input("숫자와 연산자를 입력하세요(ex:1 + 1) : ")
# num1, operator, num2 = inputs.split()

# print(calc(float(num1), float(num2), operator))


# def makeReceipt(menus):
#     text = []

#     text.append("=" * 40)

#     text.append(f"새우깡 구매 개수: {getShrimpPrice(menus)}")
#     text.append(f"비비빅 구매 개수: {getBibibigPrice(menus)}")
#     text.append(f"초코파이 구매 개수: {getChocopiePrice(menus)}")
#     text.append(f"맛동산 구매 개수: {getMatdongsanPrice(menus)}")

#     totalPrice = 0
#     for value in menus.values():
#         totalPrice += value

#     text.append("=" * 40)
#     text.append(f"총 구매 가격: {totalPrice}")
#     text.append("=" * 40)

#     return "\n".join(text)


# def getShrimpPrice(menus):
#     return menus[("새우깡", 1200)]


# def getBibibigPrice(menus):
#     return menus[("비비빅", 400)]


# def getChocopiePrice(menus):
#     return menus[("초코파이", 500)]


# def getMatdongsanPrice(menus):
#     return menus[("맛동산", 1500)]


# menus = {
#     ("새우깡", 1200): 0,
#     ("비비빅", 400): 0,
#     ("초코파이", 500): 0,
#     ("맛동산", 1500): 0,
# }

# inputs = input("갯수 입력(4개): ")
# cnt = inputs.split()

# index = 0
# for key in menus:
#     _, cost = key
#     menus[key] = int(cnt[index]) * cost
#     index += 1

# print(makeReceipt(menus))
