# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:48:18 2021

@author: zzl
"""

import os

def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    return str(files)

