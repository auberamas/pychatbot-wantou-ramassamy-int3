# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:25:11 2023

@author: aube
"""

class Colors: 
    darkgrey = (26,31,40)
    blue = (142,229,238)
    green = (118,238,198)
    red = (205,51,51)
    yellow = (255,236,139)
    orange = (255,165,79)
    purple = (212,212,246)
    darkblue = (70,100,139)
    white = (255,255,255)
    teal = (0,118,118)
    lighteal = (120,180,180)
    
    @classmethod
    def get_colors(cls):
        return[cls.darkgrey, cls.blue, cls.green, cls.red, cls.yellow, cls.orange, cls.purple, cls.darkblue]