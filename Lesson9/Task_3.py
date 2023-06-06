# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

from pathlib import Path

def calculate_summ_purchases():

    prices_file = open(Path(Path.cwd(), 'test_file', 'task_3.txt'))
    summ_list = []

    prices_list = prices_file.readlines()

    summ = 0
    for price in prices_list:
        if price == '\n':
            summ_list.append(summ)
            summ = 0
        else:
            summ += int(price[:-1])

    prices_file.close()

    summ_list.sort()
    summ_purchases = sum(summ_list[-3:])

    return summ_purchases


three_most_expensive_purchases = calculate_summ_purchases()

assert three_most_expensive_purchases == 202346

