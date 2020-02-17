#!/usr/bin/env python
#_*_coding:utf-8_*_


class dog:
    def __init__(self,name):
        self.name = name

d = dog('egon')

print(hasattr(d,"__init__"))





