#!/usr/bin/env python3.6
from parameterized import parameterized
from lab1 import BaseTest
from typing import *
import argparse, random
from subprocess import *


def mem_dict(filename: str) -> Dict[str, List[str]]:
    d = dict()
    try:
        with open(filename, 'r') as f:
            t = f.read().split()
            for i in range(len(t)):
                if t[i] not in d.keys():
                    d[t[i]] = t[i + 1:]
    except IOError:
        print('I/O error')
    except ValueError:
        print("Could not convert data")
    return d


def make_text(d: Dict[str, List[str]]):
    l = len(d) * 2
    f = True
    k = random.choice(list(d.keys())[:-1])
    a = []  # type: List[str]
    while f:
        k = random.choice(d[k])
        a.append(k)
        l -= 1
        f = d[k] != []
    return a


def main():
    """Прочитать из файла (имя - параметр командной строки)
    все слова (разделитель пробел)

    Создать "Похожий" словарь который отображает каждое слово из файла
    на список всех слов, которые следуют за ним (все варианты).

    Список слов может быть в любом порядке и включать повторения,
    например "and" ['best", "then", "after", "then", ...]

    Считаем , что пустая строка предшествует всем словам в файле.

    С помощью "Похожего" словаря сгенерировать новый текст
    похожий на оригинал.

    Т.е. напечатать слово - посмотреть какое может быть следующим и выбрать случайное."""
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('FILE', help='File to read', type=argparse.FileType('r'))
    args = parser.parse_args()
    d = mem_dict(args.FILE.name)
    print(' '.join(make_text(d)))


if __name__ == '__main__':
    main()
