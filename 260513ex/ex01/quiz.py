# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기

# numList = [3, 7, 1, 9, 5]

# maxNum = 0

# for num in numList:
#     if num > maxNum: maxNum = num

# print(maxNum)


# ------------------------------------------------------------------


# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

# n = int(input("숫자 입력: "))

# sum = 0

# for cnt in range(1, n + 1):
#     sum += cnt

# print(sum)
# print(int(n * (n + 1) / 2))


# ------------------------------------------------------------------


# 3. 리스트에 있는 숫자 중 짝수만 출력하기

# listNum = [1,2,3,4,5,6]

# for num in listNum:
#     if num % 2 == 0: print(num)


# ------------------------------------------------------------------


# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]

# listNum = [5, 1, 7, 3]
# listNum.sort()
# print(listNum)


# ------------------------------------------------------------------


# 5. 리스트 숫자를 내림차순 정렬하기
#  [5,1,7,3]

# listNum = [5, 1, 7, 3]
# listNum.sort(reverse=True)
# print(listNum)


# ------------------------------------------------------------------


# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]

# listNum = [10, 20, 30]

# # sum = 0
# # for num in listNum:
# #     sum += num

# # print(sum / len(listNum))


# ------------------------------------------------------------------


# 7. 리스트에서 가장 작은 숫자 찾기
#  (min() 사용 금지)

# numList = [3, 7, 1, 9, 5]

# minNum = numList[0]

# for num in numList:
#     if num < minNum: minNum = num

# print(minNum)


# ------------------------------------------------------------------


# 8. 1부터 100까지 숫자 중
# 3의 배수와 5의 배수 출력하기

# for cnt in range(1, 101):
#     if cnt % 3 == 0 or cnt % 5 == 0:
#         print(cnt)


# ------------------------------------------------------------------


# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]

# userList = []
# inputValue = 1

# while inputValue:
#     inputValue = int(input('숫자 입력: '))
#     userList.append(inputValue)

# userList.pop()
# print(userList)
