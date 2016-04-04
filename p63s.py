# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:22:04 2016

@author: yiyuezhuo
"""
import math

def p63():
    rl=[]
    for i in range(1,101):
        tl=[]
        for j in range(1,10):
            if len(str(j**i))==i:
                tl.append(j)
        if len(tl)>0:
            print 'check',i,'hit','j',j,'i',i,'=',j**i
            rl.extend(tl)
    print rl
    return len(rl)
    
def p64_second(x=23,plus=0,denominator=1):
    i=0
    while True:
        test=i*denominator-plus
        if test>0 and test**2>x:
            i-=1
            break
        i+=1
    surplus=plus-i*denominator
    return i,x,surplus,denominator
    
def p64_first(x=23,surplus=-3,denominator=7):
    new_denominator=(x-surplus**2)/denominator
    return x,-surplus,new_denominator
    
def p64_iter(x):
    i,x,surplus,denominator=p64_second(x,0,1)
    yield i
    while True:
        x,plus,denominator=p64_first(x,surplus,denominator)
        i,x,surplus,denominator=p64_second(x,plus,denominator)
        yield i
        
def p64_self_check(x):
    history=[]
    history.append((x,0,1))
    i,x,surplus,denominator=p64_second(x,0,1)
    while True:
        x,plus,denominator=p64_first(x,surplus,denominator)
        history.append((x,plus,denominator))
        for index,h in enumerate(history[::-1][1:]):
            if h==history[-1]:
                return index+1
        i,x,surplus,denominator=p64_second(x,plus,denominator)

        
def p64_cut(x,maxiter=10):
    rl=[]
    for index,i in enumerate(p64_iter(x)):
        if index>maxiter:
            break
        rl.append(i)
    return rl

def p64_circle(l):
    for i in range(len(l)/2):
        if l[-i:]==l[-2*i:-i]:
            return i
    return None
    
def p64_is_square(x):
    y=math.sqrt(x)
    return y==int(y)
    
def p64_period(x):
    al=[]
    for a in p64_iter(x):
        al.append(a)
        test=p64_circle(al)
        if test:
            return test

def p64_solve(itermax=10000):
    rl=[]
    for i in range(itermax+1):
        if not(p64_is_square(i)):
            rl.append((i,p64_self_check(i)))
    return rl