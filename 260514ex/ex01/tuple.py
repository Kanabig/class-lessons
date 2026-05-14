# sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

# for i, item in enumerate(sports):
#     if i % 2 != 0:
#         print(i, item)

# print(sports.index('야구'))

# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# who = input('이름: ')
# idx = names.index(who)
# print(idx)

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print('Green' not in colors)

# scores = ('A', 'A+', 'B', 'B-', 'F')
# print('경고' if 'F' in scores else '')

# nums1 = (1, 2, 3)
# nums2 = (4, 5, 6)

# print(nums1 + nums2)

# nums1 = [1, 2, 3]
# nums2 = []

# # for num in nums1:
# #     nums2.append(num)

# # nums2 = nums1[:]

# import copy

# nums2 = copy.deepcopy(nums1)

# nums1[0] = 100

# print(nums1)
# print(nums2)

# animals = ('호랑이', '사자', '곰', '여우', '늑대')
# print(f'animals: {animals}')

# print(f'animals[:3]: {animals[:3]}')

# '''
# fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
#  - 인덱스 2부터 4까지의 아이템을 출력하시오.
#  - 인덱스 0부터 3까지의 아이템을 출력하시오.
#  - 인덱스 3부터 끝까지의 아이템을 출력하시오.
# '''

# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')

# print(fruits[2:5])
# print(fruits[:4])
# print(fruits[3:])

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# colors = list(colors)
# colors.sort()
# colors = tuple(colors)
# print(colors)

# colors = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple")
# clr = sorted(colors)
# clr.reverse()
# print(clr)
