#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:46:33 2020

@author: roberthsu2003
"""
import student as sd

if __name__ == '__main__':
    stu1 = sd.getStudent()
    stu1.name = '徐國堂'
    stu1.chinese = 98
    stu1.english = 76
    stu1.math = 85
    stu1.descript()
    print('-------------------')
    stu2 = sd.getStudent()
    stu2.name = 'robert'
    stu2.chinese = 76
    stu2.english = 71
    stu2.math = 91
    stu2.descript()
