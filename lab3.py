#!/usr/bin/env python3
from parameterized import parameterized
from lab1 import BaseTest
import re


# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing",
# если в конце нет уже "ing", иначе добавить "ly".
def v(s: str) -> str:
    return s + ('ly' if s[-3:] == 'ing' else 'ing')


# 2.
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!
def nb(s: str) -> str:
    return re.sub(r'\bnot\b.*?\bbad\b', 'good', s)


class Task1(BaseTest):
    @parameterized.expand([
        ('empty', v, 'ing', ''),
        ('example', v, 'ingly', 'ing')])
    def test(self, *args):
        self.print_test(*args)


class Task2(BaseTest):
    @parameterized.expand([
        ('empty', nb, '', ''),
        ('example', nb, 'This music is good!', 'This music is not so bad!')])
    def test(self, *args):
        self.print_test(*args)
