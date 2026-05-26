import random

LIMIT = 45
NUMBER_COUNT = 6

random_numbers = []
user_numbers = []


def setUserNumbers(numbers):
    global user_numbers
    user_numbers = numbers


def getUserNumbers():
    return user_numbers


def setRandomNumbers():
    global random_numbers
    random_numbers = random.sample(range(0, LIMIT + 1), NUMBER_COUNT)


def getRandomNumbers():
    return random_numbers


def getMatchedNumbers():
    matches = [x for x in user_numbers if random_numbers.count(x) > 0]
    return matches
