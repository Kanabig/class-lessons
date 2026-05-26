import time


# 1. 공통으로 쓸 부가 기능(Aspect)을 딱 한 번만 정의합니다.
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 부가 기능: 시작 시간 기록

        result = func(*args, **kwargs)  # 🎯 원래 핵심 기능 실행!

        print(
            f"[{func.__name__}] 실행 시간: {time.time() - start_time:.4f}초"
        )  # 부가 기능: 소요 시간 출력
        return result

    return wrapper


# 2. 원하는 핵심 비즈니스 로직에 깃발(@)만 꽂아줍니다.
@measure_time
def order_item():
    print("상품을 주문합니다.")


@measure_time
def pay():
    print("결제를 진행합니다.")


# 실행해보기
order_item(1, 2)
pay()
