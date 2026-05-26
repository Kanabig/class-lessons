import random

DICE_COUNT = 5
PLAYER_COUNT = 6


class Dice:
    def __init__(self):
        self.numbers = []

    def playDice(self):
        for i in range(DICE_COUNT):
            self.numbers.append(random.randint(1, 6))

    def getNumbers(self):
        return self.numbers

    def getSum(self):
        return sum(self.numbers)


if __name__ == "__main__":

    dices = []
    scores = []

    for cnt in range(PLAYER_COUNT):
        dices.append(Dice())
        dices[cnt].playDice()

    for cnt in range(PLAYER_COUNT):
        print(f"gamer{cnt + 1}: {dices[cnt].getNumbers()}")
        print(f"sum of gamer{cnt + 1}: {dices[cnt].getSum()}")
        print("-" * 30)
        scores.append(dices[cnt].getSum())

    print("=" * 30)

    scores.sort(reverse=True)
    for cnt, score in enumerate(scores):
        cnt += 1
        text = f"{cnt}등: {score} " + ("WIN!" if cnt == 1 else "")
        print(text)

    print("=" * 30)
