#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:51:35 2020

@author: roberthsu2003
"""
#參數傳入的是不可以變的實體
def turbo(s):
    print('加速前速度:', s)
    s += 10
    return s


if __name__ == "__main__":
    speed = int(input("請輸入初始速度:"))
    speed = turbo(speed)
    print('加速後的速度:',speed)

