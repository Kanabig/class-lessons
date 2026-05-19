# def forecastWeather(temp, humi, rain):
#     print(temp, humi, rain)
#     pass


# forecastWeather(10, 10, 10)


# def printScoresForStudents(*args):
#     numbers = []

#     if isinstance(args[0], (list, tuple)):
#         numbers = args[0]
#     else:
#         numbers = args

#     totalScore = 0

#     for score in numbers:
#         totalScore += score

#     print(totalScore, totalScore / len(numbers))


# studentScores = []

# isRunning = True

# while isRunning:
#     data = int(input("학생의 점수: "))

#     if data == -1:
#         isRunning = False

#     studentScores.append(data)

# printScoresForStudents(studentScores)


# quiz) SMS와 MMS 구별하기


"""
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다.
"""

# SMS_LENGTH_LIMIT = 50


# def sendMessage(text):
#     cost = 0
#     isSms = True

#     if len(text) <= SMS_LENGTH_LIMIT:
#         cost = 50
#     else:
#         cost = 100
#         isSms = False

#     print(cost, "SMS" if isSms else "MMS")


# text = input("문자 입력: ")
# sendMessage(text)


# def forecastWeather(temp=10, humi=10, rain=10):
#     print(temp, humi, rain)


# forecastWeather(27, rain=99)


# for cnt in range(1, 7 + 1):
#     print("*" * cnt)

# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
