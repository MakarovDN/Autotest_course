# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("args, result", [
    pytest.param((10, 5), 2),
    ((100, 25), 4),
    pytest.param((10, 0, 2), None, marks=pytest.mark.skip(reason="Skipping division zero")),
])
def test_division(args, result):
    assert all_division(*args) == result
