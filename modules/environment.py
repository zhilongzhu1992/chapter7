# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:51:05 2021

@author: zzl
"""

import os

def run(**args):
    print("[*] In environment module.")
    return str(os.environ)
