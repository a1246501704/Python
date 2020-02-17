#! /usr/bin/env python
# -*- coding=utf-8 -*-

import itertools

list1 = [1,2,3,4,5]

list2 = []
list3 = []

for i in range(1, len(list1) + 1):
    iter = itertools.permutations(list1, i)

    list2.append(list(iter))
    list2=list2[-1]
    # print(list2)
    # print(list2[-1])
    for item in list2:
        # print(len(item))
        if len(item) == 5:
            # print(item)
            list3.append(item)
    # for item in list3:
    #     print(item)
    print(len(list3))
    # print(list3)




