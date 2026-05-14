# for i in range(1, 101):
#     times = 0
#     place_ten = i // 10
#     place_one = i % 10

#     if (place_one % 3 == 0) and (place_one != 0): times += 1
#     if (place_ten % 3 == 0) and (place_ten != 0): times += 1

#     print(f'{i}{', 짝!' * times}')


# -----------------------------------------------------------------


# 오전 9 ~ 오전 6시 
# 3대의 열차가 교차하는 시간 구하기
# A = 첫차 오전 9시 ~ 막차 오후 6시 / 운행간격 10분
# B = 첫차 오전 9시 ~ 막차 오후 6시 / 운행간격 25분
# C = 첫차 오전 9시 ~ 막차 오후 6시 / 운행간격 30분

# TRAIN_A = 10
# TRAIN_B = 25
# TRAIN_C = 30
# START_HOUR = 9
# MINUTE = 60

# 540 ~ 1080. 실제 시작 시간에 맞춰보기.
# end = 540

# crash_a = False
# crash_b = False
# crash_c = False

# for t in range(end):
#     crash_a = t % TRAIN_A == 0
#     crash_b = t % TRAIN_B == 0
#     crash_c = t % TRAIN_C == 0

#     if crash_a and crash_b: print(f'a_b : {t // MINUTE + START_HOUR}시, {t % MINUTE}분')
#     if crash_a and crash_c: print(f'a_c : {t // MINUTE + START_HOUR}시, {t % MINUTE}분')
#     if crash_b and crash_c: print(f'b_c : {t // MINUTE + START_HOUR}시, {t % MINUTE}분')


# -----------------------------------------------------------------


# ADMIM_PWD = '12345'
# MAX_WRONG_COUNT = 5

# wrong_count = 0

# while True:
#     inputs = input('비밀번호를 입력하세요: ')
    
#     if ADMIM_PWD == inputs: 
#         print('로그인 되었습니다.')
#         break
#     else:
#         print('로그인 실패.')
#         wrong_count += 1

#     if wrong_count >= MAX_WRONG_COUNT:
#         print('로그인 횟수 초과')
#         break


# -----------------------------------------------------------------


# count = int(input('양수 입력: '))
# sum = 1

# for count in range(1, count + 1):
#     sum *= count 

# print(f'{count}! = {sum}')


# -----------------------------------------------------------------


# import random

# random.randrange

# WIN_TEXT = '정답입니다.'
# LOOSE_TEXT = '게임에서 지셨습니다.'

# OPPORTUNITY = 10
# ANSWER = random.randint(0, 100)
# attempts = 0

# max_range = 100
# min_range = 0

# result_text = ''

# while True:
#     # FIXME: guess = 숫자가 아닌 값 예외처리, 범위 밖의 값 예외처리
#     prompt = f'남은 기회: {OPPORTUNITY - attempts}번\n'
#     prompt += f'숫자를 입력하세요({min_range} ~ {max_range}): '
#     guess = int(input(prompt))
#     attempts += 1
    
#     if ANSWER == guess:
#         result_text = WIN_TEXT
#         break

#     if OPPORTUNITY <= attempts:
#         result_text = LOOSE_TEXT
#         break

#     # prompt = (min_range ~ max_range) 수정
#     if ANSWER < guess:
#         if guess < max_range: max_range = guess
#     else:
#         if guess > min_range: min_range = guess


# print(f'{result_text} 난수: {ANSWER}')


# -----------------------------------------------------------------


# WIDTH_STEP = 2
# HEIGHT_STEP = 3
# MAX_RECT = 150

# minRect = 10000
# maxRect = 0

# width = 1
# height = 1
# cnt = 0

# while width * height <= MAX_RECT:
#     crtRect = width * height
    
#     if minRect > crtRect: minRect = crtRect
#     if maxRect < crtRect: maxRect = crtRect
    
#     print(width, height)
#     print(f'최소: {minRect}, 최대: {maxRect}')
    
#     cnt += 1
#     width = WIDTH_STEP * cnt
#     height = HEIGHT_STEP * cnt
    

# -----------------------------------------------------------------

