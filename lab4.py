#!/usr/bin/env python3.6
from parameterized import parameterized
from lab1 import BaseTest
from typing import *
from lxml import html
import argparse


def extr_name(filename: str) -> Dict[str, Any]:
    """Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
    '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д."""
    male = dict()
    female = dict()
    y = 2000
    try:
        with open(filename, 'r') as f:
            b = html.fromstring(f.read())
            y = int(b.xpath('//h2|//h3')[0].text[-4:])
            trs = b.xpath('//table[@summary="Popularity for top 1000"]//tr')[1:-1]
            for tr in trs:
                tds = tr.xpath('./td')
                male[int(tds[0].text)] = tds[1].text
                female[int(tds[0].text)] = tds[2].text
    except IOError:
        print(f'I/O error')
    except ValueError:
        print("Could not convert data")
    return {'male': male, 'female': female, 'year': y}


def main():
    """Для каждого переданного аргументом имени файла, вывести имена  extr_name
    напечатать ТОП-10 муж и жен имен из всех переданных файлов"""
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--top10', '-t', action='store_true')
    parser.add_argument('FILE', nargs='+', help='File to read', type=argparse.FileType('r'))
    parser.add_argument('--file', '-f', action='append', help='File to read', type=argparse.FileType('r'))
    args = parser.parse_args()
    print(args)
    for fname in args.FILE + (args.file if args.file else []):
        d = extr_name(fname.name)
        if args.top10:
            print(f'Top 10 from {fname.name} in {str(d["year"])} year:')
            print(' {0:3} {1:11} {2:11}'.format('Num', 'Male', 'Female'))
            for i in range(1, 11):
                print(f' {i:3d} {d["male"][i]:11s} {d["female"][i]:11s}')
        else:
            m = sorted([f'{v} {str(k)}' for (k, v) in d['male'].items()])
            f = sorted([f'{v} {str(k)}' for (k, v) in d['female'].items()])
            print(f'Alphabetic from {fname.name} in {str(d["year"])} year:')
            print(' Male names:')
            for i in m[:21]:
                print(f'  {i}')
            print(' Female names:')
            for i in m[:21]:
                print(f'  {i}')
            pass


if __name__ == '__main__':
    main()
