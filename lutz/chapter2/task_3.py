#! /usr/bin/env python3
# -*- coding: utf-8 -*-

L = [1, 2, 3, 4]
L[2] = []
print(L)
L[2:3] = []
print(L)
del L[0]
print(L)
del L[1:]
print(L)
# L[1:2] = 1
print(L)
