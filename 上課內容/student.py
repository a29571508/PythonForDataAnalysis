#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:25:41 2020

@author: roberthsu2003
"""
def getStudent():
    return Student();

class Student:
    #初始化
    def __init__(self):
        #實體屬性
        self.name=""
        self.chinese=0
        self.english=0
        self.math=0
    
    #實體方法
    def descript(self):
        print('name', self.name)
        print('chinese', self.chinese)
        print('english', self.english)
        print('math', self.math)
        