# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 08:29:41 2016

@author: yiyuezhuo
"""
import math

def _p65(seq):
    if len(seq) == 1:
        return (1, seq[0])
    head = seq[0]
    numerator,denominator = _p65(seq[1:])
    return (denominator, head * denominator + numerator)
def p65(seq):
    return _p65(seq)[::-1]
def cf2_seq(n):
    return [1]+[2]*(n-1)
def cf2(n):
    return p65(cf2_seq(n))
    
def cfe_seq(n):
    seq = [2]
    for i in range(n-1):
        if i % 3 == 0:
            seq.append(1)
        elif i % 3 == 1:
            seq.append( 2*((i - 1)//3 + 1) )
        else:
            seq.append(1)
    return seq
def cfe(n):
    return p65(cfe_seq(n))
    
def p66(D, max_iter = 100000):
    for x in range(2, max_iter):
        y = math.sqrt((x**2 - 1) / D)
        if y % 1 == 0:
            return (x,y)
    raise Exception
    
def p66_iter(maxD):
    rl = []
    for D in range(2, maxD+1):
        if math.sqrt(D) % 1 != 0:
            try:
                rl.append(p66(D))
            except:
                pass
    return rl