"""
사용자가 3과목의 시험 점수를 입력하면 총점, 평점, 통과 여부를 출력하는 프로그램을 모듈을 이
용해서 만들어 봅시다. 시험 통과 여부는 평점이 60이상이고 한 과목도 40미만이 없다면 ‘Pass’,
그렇지 않으면 ‘Fail’로 판정합니다.
"""


def get_total_score(scr1, scr2, scr3):
    return scr1 + scr2 + scr3


def get_average_score(scr1, scr2, scr3):
    return get_total_score(scr1, scr2, scr3) / 3


def is_passed(scr1, scr2, scr3):
    if get_average_score(scr1, scr2, scr3) >= 60:
        if scr1 >= 40 and scr2 >= 40 and scr3 >= 40:
            return True

    return False
