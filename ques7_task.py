# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:36:43 2021

@author: Aryan Sharma
"""


import sys
import string

def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

n=int(sys.argv[1])
res = string.ascii_lowercase[:n]

print(res)
a = list(res)
permute(a,0,n-1)
