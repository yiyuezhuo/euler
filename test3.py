# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:07:15 2016

@author: yiyuezhuo
"""

def p55_iter(n):
    m=list(str(n))
    m.reverse()
    m=int(''.join(m))
    return n+m
    
def p55_is_palindromic(n):
    s=str(n)
    length=len(s)
    for i in range(length):
        if s[i]!=s[length-i-1]:
            return False
    return True
    
def p55(limit=10000):
    match_l=[]
    for i in range(limit):
        n=i
        for j in range(50):
            n=p55_iter(n)
            if p55_is_palindromic(n):
                match_l.append(n)
                break
    return limit-len(match_l)
#249
    
def p56():
    rl=[]
    for a in range(100):
        for b in range(100):
            rl.append(sum(map(lambda x:int(x),str(a**b))))
    return max(rl)
    
def p57_seq():
    seq=[(5,2)]
    for i in range(999):
        right,left=seq[-1]
        left+=2*right
        seq.append((left,right))
    seq=[(left-right,right) for left,right in seq]
    return seq
    
def p57():
    seq=p57_seq()
    return sum([len(str(left))>len(str(right)) for left,right in seq])
    