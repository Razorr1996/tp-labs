#!/usr/bin/env python3
from parameterized import parameterized
from lab1 import BaseTest
from typing import List, Tuple, Any, Callable


# 1.
def rm_adj(nums: List):
    """:param nums: Список чисел
    :return: Список чисел, где повторяющиеся числа урезаны до одного[0, 2, 2, 3] -> [0, 2, 3]"""
    return list(set(nums))


# 2.
def mrg(list1: List, list2: List):
    """:param list1: Список
    :param list2: Список
    :return: Новый отсортированный объединенный список"""
    return sorted(list1 + list2)


class Task1(BaseTest):
    @parameterized.expand([
        ('empty', rm_adj, [], []),
        ('example', rm_adj, [0, 2, 3], [0, 2, 2, 3])])
    def test(self, *args):
        self.print_test(*args)


class Task2(BaseTest):
    @parameterized.expand([
        ('empty', mrg, [], [], []),
        ('small', mrg, [0, 1, 1, 2], [0, 1], [1, 2]),
        ('example', mrg, [0, 1, 2, 3, 4, 5, 6, 7, 10, 12], [1, 2, 4, 7, 10], [0, 3, 5, 6, 12])])
    def test(self, *args):
        self.print_test(*args)


if __name__ == '__main__':
    print('Lab2')
