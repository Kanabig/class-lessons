# def convertUnit(length_mm):
#     units = {
#         "cm": length_mm * 0.1,
#         "m": length_mm * 0.001,
#         "inch": length_mm * 0.03937,
#         "feet": length_mm * 0.003281,
#     }

#     return units


# def printLength(unit_lengths):
#     for unit in unit_lengths:
#         print(f"{unit}: {unit_lengths[unit]:<.2f}{unit}")


# length = int(input("길이: "))

# units = convertUnit(length)
# printLength(units)

"""
DW마트는 고객 감사의 일환으로 ‘오늘의 할인’ 이벤트를 진행할 계획입니다. 아래
의 상품 가격표를 참고해서 ‘오늘의 할인율’을 입력하면 할인된 가격이 출력되는 프
로그램을 만들어 봅시다.
쌀9900
상추1900
고추2900
마늘8900
통닭5600
햄6900
치즈3900
"""

# menus = {
#     "쌀": 9900,
#     "상추": 1900,
#     "고추": 2900,
#     "마늘": 8900,
#     "통닭": 5600,
#     "햄6": 900,
#     "치즈": 3900,
# }


# def get_discount_price(discount_rate):
#     menu_and_dc_price = {}
#     for menu_name, price in menus.items():
#         dc_price = int(price * (1 - (discount_rate / 100)))
#         menu_and_dc_price[menu_name] = dc_price

#     return menu_and_dc_price


# def print_price(menu_and_prices):
#     for menu_name, price in menu_and_prices.items():
#         print(f"{menu_name}: {menus[menu_name]}, 할인가: {price}원")


# print_price(menus)
# discount_rate = int(input("오늘의 할인율: "))
# print_price(get_discount_price(discount_rate))
