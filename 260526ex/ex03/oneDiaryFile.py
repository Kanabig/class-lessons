import config
import time


def write():
    timeStemp = time.strftime("%Y-%m-%d, %H:%M:%S")
    text = input(f"\n[{timeStemp}] 한줄 일기를 작성하세요\n: ")

    with open(config.PATH, "a", encoding="utf-8") as file:
        file.write(f"{timeStemp}: {text}\n")


def read():
    with open(config.PATH, encoding="utf-8") as file:
        text = file.read()

    print(f"\n{text}")


onRunning = True
while onRunning:
    selected = input("\n1. 일기작성 | 2. 일기조회 | 0. 종료\n: ")

    if config.WRITE == selected:
        write()
    elif config.READ == selected:
        read()
    elif config.EXIT == selected:
        onRunning = False
    else:
        print("\n정상적인 명령어를 입력해주세요!")
