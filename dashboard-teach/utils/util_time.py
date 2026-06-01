from datetime import datetime


def getCurrentDateTime():
    return datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
