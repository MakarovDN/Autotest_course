# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time

@pytest.mark.usefixtures("time_start")
class TestClass:
    def test_1(self):
        time.sleep(1)
        assert 1 + 1 == 2


    def test_2(self, time_stop):
        time.sleep(2)
        assert 1 + 1 == 2


    def test_3(self):
        time.sleep(3)
        assert 1 + 1 == 2

