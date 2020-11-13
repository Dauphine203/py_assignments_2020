#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:36:10 2020

@author: raphoucs
"""
import pytest

@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_3(input_value): #input_value):
   assert input_value % 3 == 0

#def test_divisible_by_6(input_value): #input_value):
#   assert input_value % 6 == 0