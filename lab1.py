#!/usr/bin/env python3
import unittest
from functools import reduce
from typing import List, Tuple, Any, Callable
from parameterized import parameterized


# 1.
def me(words: List[str]) -> int:
    """:param words: Cписок строк
    :return: Количесво строк где длина строки > 2 символов и первый символ равен последнему"""
    return reduce(lambda a, k: a + (len(k) > 2 and k[0] == k[-1]), words, 0)


# 2.
def fx(words: List[str]) -> List[str]:
    """:param words: Cписок строк
    :return: Cписок со строками (упорядочено) за исключением всех строк начинающихся с'x',
    которые попадают в начало списка.
    ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']"""
    return sorted(words, key=lambda k: (k[0] != 'x', k))


# 3.
def tp(tuples: List[Tuple[Any, ...]]) -> List[Tuple]:
    """:param tuples: Список непустых кортежей
    :return: Список, сортированный по возрастанию последнего элемента в каждом кортеже
    [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]"""
    return sorted(tuples, key=lambda k: k[-1])


class BaseTest(unittest.TestCase):
    def print_test(self, name: str, m: Callable, exp, *args):
        print("{0}{1} = {2}".format(m.__name__,str(args[:]),str(exp)))
        self.assertEqual(m(*args), exp)


class Task1(BaseTest):
    @parameterized.expand([
        ('empty', me, 0, []),
        ('one', me, 0, ['a']),
        ('two', me, 0, ['aa']),
        ('three', me, 1, ['aaa']),
        ('three', me, 2, ['asa', 'bvb']),
        ('some', me, 3, ['a', 'aa', 'vsv', 'hhh', 'asdasdasdsfa'])])
    def test(self, *args):
        self.print_test(*args)


class Task2(BaseTest):
    @parameterized.expand([
        ('empty', fx, [], []),
        ('example', fx, ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix'], ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'])])
    def test(self, *args):
        self.print_test(*args)


class Task3(BaseTest):
    @parameterized.expand([
        ('empty', tp, [], []),
        ('example', tp, [(2, 2), (1, 3), (3, 4, 5), (1, 7)], [(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
        ('sort', tp, [(0, 2), (0, 3), (0, 5), (0, 7)], [(0, 7), (0, 3), (0, 5), (0, 2)])])
    def test(self, *args):
        self.print_test(*args)


if __name__ == '__main__':
    print('Lab1')
