import lotto_ex as lm

if __name__ == "__main__":
    lm.setRandomNumbers()

    nums = []

    print("1부터 45까지의 정수 6개를 입력하세요.")
    nums.append(int(input(": ")))
    nums.append(int(input(": ")))
    nums.append(int(input(": ")))
    nums.append(int(input(": ")))
    nums.append(int(input(": ")))
    nums.append(int(input(": ")))

    lm.setUserNumbers(nums)

    # lm.random_numbers = [1, 2, 3, 4, 5, 6]
    # lm.user_numbers = [4, 5, 6, 7, 8, 9]

    print(f"이번주 로또 번호: {lm.getRandomNumbers()}")
    print(f"내 로또 번호: {lm.getUserNumbers()}")
    print(f"일치하는 번호: {lm.getMatchedNumbers()}")
