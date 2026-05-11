# class MyRange:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if  self.current < self.end:
#             result = self.current
#             self.current += 1
#             return result
#         else:
#             raise StopIteration


# for i in MyRange(0, 5):
#     print(f'i : {i}')


# -----------------------------------------------------------------


# # quiz
# for num in range(1, 16):
#     if (num <= 8) and (num % 2 == 0):
#         print(num)


# -----------------------------------------------------------------


# num = int(input('횟수 입력: '))

# for count in range(num):
#     print(f'메일 발송!: {count + 1}회.')


# -----------------------------------------------------------------


# for i in range(1, 11):
#     print('3의 배수!' if (i % 3 == 0) else i)


# -----------------------------------------------------------------


# # ex1
# num = int(input('구구단을 외자~!: '))

# for i in range(1, num + 1):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j}')

#     print('---------\n')

# # ex2
# num = int(input('구구단을 외자: '))

# for i in range(1, 10):
#     print(f'{num} x {i} = {num * i}')


# -----------------------------------------------------------------


# ex1
# n = int(input('1~n까지의 합(n 입력): '))
# print(f'{int(n * (n + 1) / 2)}')

# # ex2
# sum = 0

# for i in range(1, n + 1):
#     sum += i

# print(sum)


# -----------------------------------------------------------------


# min = 0

# for num in range(1, 101):
#     if (num % 3 == 0) and (num % 7 == 0):
#         if (min == 0): min = num
#         print(num)

# print(f'최소공배수: {min}')


# -----------------------------------------------------------------

# cnt = 1
# while (cnt < 10):
#     num = 2
#     while (num < 10):
#         # <2는 2자리 확보 후 좌측 정렬
#         print(f'{num} x {cnt} = {num * cnt:<2}', end=' | ')
#         num += 1
    
#     # 줄넘김
#     print()
#     cnt += 1

# -----------------------------------------------------------------

# cnt = 1
# min = 0

# while cnt < 101:
#     if (cnt % 3 == 0) and (cnt % 8 == 0):
#         print(f'{cnt}')
#         if (min == 0): min = cnt

#     cnt += 1

# print(f'최소공배수: {min}')


# -----------------------------------------------------------------


# cnt = 1
# area = 0

# while area < 150:
#     area = (cnt * 2) * (cnt * 3) / 2
#     print(area)
#     cnt += 1


# -----------------------------------------------------------------