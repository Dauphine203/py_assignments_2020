#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:17:33 2020

@author: raphoucs
"""

def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('Raphael') == 'Hello Raphael'

