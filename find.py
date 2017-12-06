#!/usr/bin/env python3
from functools import lru_cache
from urllib import parse
from random import choice, choices, getrandbits
import requests
from lxml import html
from typing import List
from os.path import join


@lru_cache(maxsize=1)
def get_famous_names() -> List[str]:
    h = html.parse(join('ext', 'famous-100.html'))
    rows = h.xpath('//article/section/ol[1]/li')
    names = []
    for i in rows:
        inner = i.xpath('a')
        t = (inner[0] if inner else i).text_content().split()
        for w in range(len(t)):
            if '(' == t[w][0]:
                t = t[:w]
                break
        names.append(' '.join(t))
    return names


@lru_cache()
def get_images(name: str) -> List[str]:
    url = 'https://www.google.ru/search?tbm=isch&gbv=1&newwindow=1&q=%s+face' % parse.quote_plus(name)
    raw_images = html.fromstring(requests.get(url).text).xpath('//a/img')
    return [i.attrib['src'] for i in raw_images]


class Game:
    names = get_famous_names()

    def __init__(self, level: int = 1):
        m = 10
        if level == 2:
            m = 50
        elif level == 3:
            m = 100
        _n = Game.names[:m]
        self.name = choice(_n)
        self.pic = choice(get_images(self.name))
        _s = set(choices(_n, k=3) + [self.name])
        while len(_s) < 4:
            _s.add(choice(_n))
        self.vars = list(_s)
        self.id = getrandbits(128)

    def __repr__(self):
        return "Game '%s'" % self.name


if __name__ == '__main__':
    a = [Game(2) for i in range(5)]
    print(get_images.cache_info())
