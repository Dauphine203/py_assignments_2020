#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:50:24 2020

@author: raphoucs
"""

import pytest

def my_square(x):
    return x ** 2

@pytest.mark.parametrize('input,expected', [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
    (6, 36),
    (7, 49),
])

def test_parametrized(input, expected):
    assert my_square(input) == expected
    