# test case for decorator
import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print(f"time taken by function{end_time - start_time}")

    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function")
    time.sleep(2)
# result given in epoch time
"""
@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function")
    time.sleep(8)
"""