# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 08:11:26 2016

@author: yiyuezhuo
"""
import collections

def get_prime_by_cache():
    import pickle
    f=open('prime_numbers','rb')
    obj=pickle.load(f)
    f.close()
    return obj

def times(l):
    return reduce(lambda x,y:x*y,l)


def pick(n,sl):
    for i in sl:
        if n%i==0:
            return n/i,i
    return False

def picktopick(n,sl):
    hl=[]
    while True:
        r=pick(n,sl)
        if r==False:
            return n,hl
        else:
            hl.append(r[1])
            n=r[0]
            
def pickmap(n,sl):
    r=picktopick(n,sl)[1]
    return collections.Counter(r)
    
def picknumber(n,sl):
    c=pickmap(n,sl).values()
    cc=[i+1 for i in c]
    return  times(cc)


