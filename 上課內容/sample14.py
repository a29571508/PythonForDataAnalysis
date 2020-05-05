#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:17:38 2020

@author: roberthsu2003
"""

def turbo(s):
    s[0] += 10;
    s[1] += 10;

if __name__ == "__main__":
    speed = [50, 60]
    turbo(speed)
    print('speed[0]',speed[0])
    print('speed[1]',speed[1])