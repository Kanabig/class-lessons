# fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']

# for item in fruits:
#     if item == '당근' or item == '토마토':
#         fruits.remove(item)

# print(fruits)


# -----------------------------------------------------------------


# scores = [55, 35, 40, 70, 65, 30]

# sum = 0
# fail = 0

# for score in scores:
    
#     if score < 40:
#         fail += 1

#     sum += score

# print(f'평균: {sum / len(scores):.2f}, 과락: {fail}개')


# -----------------------------------------------------------------


# numbers = [5, 1, 2, 6, 3, 4]

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# chars = ['가', '라', '다', '마', '바', '나']

# chars.reverse()
# print(chars)

# chars.sort()
# print(chars)

# chars.sort(reverse=True)
# print(chars)


# -----------------------------------------------------------------


# fruits = ['사과', '망고', '당근', '수박', '포도']

# print(fruits[3:])
# print(fruits[:3])

# print(fruits[:-1])
# print(fruits[len(fruits) - 2:])

# print(fruits)
# print(fruits[::2])

# sliced = fruits[:]
# sliced.append('참새')
# print(fruits)
# print(sliced)


# -----------------------------------------------------------------


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# print(alphabet[2:6])
# print(alphabet[:5])
# print(alphabet[3:8])
# print(alphabet[5:])
# print(alphabet[3:9])
# print(alphabet[-4:])


# -----------------------------------------------------------------


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# del alphabet[:4]
# print(alphabet)