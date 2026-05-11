# from enum import IntEnum

# MONEY_ONE = 400000
# MONEY_TWO = 600000
# MONEY_THREE = 800000
# MONEY_OVER = 1000000

# class FamillyUnit(IntEnum):
#     ZERO = 0
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     OVER = 4

#     @classmethod
#     def _missing_(cls, value):
#         return cls.OVER if (value > 0) else cls.ZERO

# def option_select(option):
#     support_money = 0

#     match option:
#         case FamillyUnit.ZERO: support_money = 0
#         case FamillyUnit.ONE: support_money = MONEY_ONE
#         case FamillyUnit.TWO: support_money = MONEY_TWO
#         case FamillyUnit.THREE: support_money = MONEY_THREE
#         case _: support_money = MONEY_OVER

#     return support_money

# input_data = int(input('가구 인원 수: '))
# result = option_select(FamillyUnit(input_data))
# print(f'지원금: {result:,}원')


# LOW_WEIGHT_THRES= 90
# NORMAL_THRES = 110
# OVER_WEIGHT_THRES = 120
# OBESITY_THRES = 140

# input_data = int(input('BMI: '))

# if                       input_data <= LOW_WEIGHT_THRES:  print('저체중')
# elif LOW_WEIGHT_THRES  < input_data <= NORMAL_THRES:      print('정상')
# elif NORMAL_THRES      < input_data <= OVER_WEIGHT_THRES: print('과체중')
# elif OVER_WEIGHT_THRES < input_data <= OBESITY_THRES:     print('비만')
# else:                                                     print('고도비만')


# MON = 1
# TUES = 2
# WEDN = 3
# THUR = 4
# FRI = 5
# OFFSET = 5
# AGE_THRES = 65

# def getOffset(value):
#     return (value + OFFSET) % (OFFSET * 2)

# endBirthYear = int(input('출생연도 끝자리:'))
# age = int(input('나이:'))

# if age < AGE_THRES:
#     if endBirthYear == MON or endBirthYear == (MON + OFFSET):
#         print("월")
#     elif endBirthYear == TUES or endBirthYear == (TUES + OFFSET):
#         print('화')
#     elif endBirthYear == WEDN or endBirthYear == (WEDN + OFFSET):
#         print('수')
#     elif endBirthYear == THUR or endBirthYear == (THUR + OFFSET):
#         print('목')
#     elif endBirthYear == FRI or endBirthYear == getOffset(FRI + OFFSET):
#         print('금')

# else:
#     print('언제든 구매 가능')


# from datetime import datetime

# car_number = int(input('\n차량 번호 4자리를 입력하세요: '))

# date_today = datetime.today().day
# is_even_day = (date_today % 2) == 0
# is_even_car_number = (car_number % 2) == 0

# print(f'오늘 날짜: ', date_today)
# print(f'오늘 입차: 번호가 {'짝수' if is_even_day else '홀수'}인 차량')

# if is_even_day: print(f'귀하의 차량은 입차 {'가능' if     is_even_car_number else '불가능'}합니다.')
# else:           print(f'귀하의 차량은 입차 {'가능' if not is_even_car_number else '불가능'}합니다.')


# TIME_UNIT_BASIS = 60
# SURVIVE_RATIO_60_SEC = 85
# SURVIVE_RATIO_120_SEC = 76
# SURVIVE_RATIO_180_SEC = 66
# SURVIVE_RATIO_240_SEC = 57
# SURVIVE_RATIO_300_SEC = 47
# SURVIVE_RATIO_OVER = 25

# timeSpent = int(input('\n최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요: '))
# surviveRatio = 0

# #for
# if   timeSpent <= TIME_UNIT_BASIS    : surviveRatio = SURVIVE_RATIO_60_SEC
# elif timeSpent <= TIME_UNIT_BASIS * 2: surviveRatio = SURVIVE_RATIO_120_SEC
# elif timeSpent <= TIME_UNIT_BASIS * 3: surviveRatio = SURVIVE_RATIO_180_SEC
# elif timeSpent <= TIME_UNIT_BASIS * 4: surviveRatio = SURVIVE_RATIO_240_SEC
# elif timeSpent <= TIME_UNIT_BASIS * 5: surviveRatio = SURVIVE_RATIO_300_SEC
# else:                                  surviveRatio = SURVIVE_RATIO_OVER

# print(f'생존율: {surviveRatio}%')


# BILL_CAP_LEVEL1 = 200
# BILL_CAP_LEVEL2 = 400

# BILL_BASE_LEVEL1 = 910
# BILL_BASE_LEVEL2 = 1600
# BILL_BASE_LEVEL3 = 7300

# BILL_UNIT_LEVEL1 = 99.3
# BILL_UNIT_LEVEL2 = 187.9
# BILL_UNIT_LEVEL3 = 280.6

# electUsage = int(input('전기 사용량을 입력하세요: '))
# print(f'사용량: {electUsage}')

# basePrice  = 0
# billUnit   = 0

# #for
# if  electUsage < BILL_CAP_LEVEL1:
#     basePrice  = BILL_BASE_LEVEL1 
#     billUnit   = BILL_UNIT_LEVEL1

# elif electUsage < BILL_CAP_LEVEL2:
#     basePrice  = BILL_BASE_LEVEL2
#     billUnit   = BILL_UNIT_LEVEL2
    
# else:                              
#     basePrice  = BILL_BASE_LEVEL3
#     billUnit   = BILL_UNIT_LEVEL3

# totalPrice = basePrice + billUnit * electUsage

# print(f'기본 요금: {basePrice:,}원')
# print(f'단가: {billUnit:,}원')
# print(f'전기 요금: {totalPrice:,}원')

# import random

# myChoice = int(input('1.가위, 2.바위, 3.보: '))
# rndChoice = random.randint(1, 3)
# print(rndChoice)

# result = myChoice - rndChoice + 3 % 3

# if (result == 0):
#     print("무승부")
# else:
#     print("승" if result == 1 else "패")
