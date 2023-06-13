import pytest
import datetime



@pytest.fixture(scope="class")
def time_start():
    start_time = datetime.datetime.now()
    print(f"\nВремя начала тестов класса: {start_time.strftime('%H:%M:%S')}")
    yield
    end_time = datetime.datetime.now()
    print(f"\nВремя окончания тестов класса: {end_time.strftime('%H:%M:%S')}")


@pytest.fixture
def time_stop():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    exec_time = end_time - start_time
    return print(f"\nВремя выполнения теста: {round(exec_time.microseconds/10**6 , 3)} сек.")
