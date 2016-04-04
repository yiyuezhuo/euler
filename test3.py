# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:07:15 2016

@author: yiyuezhuo
"""

from factor_tool import get_prime_by_cache,picktopick
from collections import Counter,defaultdict
import itertools
import math

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
    
def p58_aspect(n):
    '''n是层数，返回那个层的四个数,1当做“第一层”'''
    last=(n*2-1)**2
    d=2*n-3
    third=last-d-1
    second=third-d-1
    first=second-d-1
    return first,second,third,last
    
def is_prime(n,prime_l):
    limit=math.sqrt(n)
    for p in prime_l:
        if p>limit:
            return True
        else:
            if n % p==0:
                return False
    
def p58(limit,prime_l):
    hit_l=[]
    for i in range(2,limit):
        ts=p58_aspect(i)
        for t in ts:
            #if t in prime_s:
            #    hit_l.append(t)
            #if len(picktopick(t,prime_l)[1])==1:
            #    print t
            #    hit_l.append(t)
            if is_prime(t,prime_l):
                #print t
                hit_l.append(t)
        total=4*i-3
        odd=float(len(hit_l))/total
        if odd<0.1:
            return i*2-1
        else:
            pass
            #print i,odd     
#p58(20000,prime_l)
#26241
            
def p59_load():
    fname='p059_cipher.txt'
    f=open(fname,'r')
    s=f.read()
    f.close()
    return [int(ss.strip()) for ss in s.split(',')]
    
def XOR(x,y):
    return (~x&y)|(x&~y)
    
def p59_decryption(key_char,obj_code):
    return chr(XOR(ord(key_char),obj_code))
    #return chr((~ord(key_char)&obj_code)|(ord(key_char)&~obj_code))
    
alphas='abcdefghijklmnopqrstuvwxyz'

def p59_try(try_number):
    for a in alphas:
        r=p59_decryption(a,try_number)
        print 'key',a,'XOR test number',try_number,'get',r
        if r in alphas:
            print r
def p59_try2(nl,length=50,trans=0):
    try_l=[nl[i] for i in range(trans,length*3+trans,3)]
    for a in alphas:
        r=[p59_decryption(a,t) for t in try_l]
        print a,'get',''.join(r)
#从中手动寻找最“不乱”的那个
#god
        
def p59_try3(key,nl,length=100):
    key=key*((length/len(key))+1)
    r=''.join([p59_decryption(key[i],nl[i]) for i in range(length)])
    return r
    
def p59():
    nl=p59_load()
    s=p59_try3('god',nl,len(nl))
    return sum([ord(i) for i in s])
#107359
def p60_valid(com,prime_s):
    for left,right in itertools.permutations(com,2):
        n=int(str(left)+str(right))
        if not(n in prime_s):
            return False
    return True
    
def p60(test_l,prime_s,number=4):
    rl=[]
    for com in itertools.combinations(test_l,number):
        if p60_valid(com,prime_s):
            rl.append(com)
    return rl
    
def p60_sub(prime_l,cut=200):
    rl=[]
    for left,right in itertools.permutations(prime_l[:cut],2):
        lefts,rights=str(left),str(right)
        n=int(lefts+rights)
        n2=int(rights+lefts)
        if is_prime(n,prime_l) and is_prime(n2,prime_l):
            rl.append((left,right))
    return rl
    
def p60_find(tl,prime_s,count=4):
    td=defaultdict(list)
    for key,value in tl:
        td[key].append(value)
    tds={key:set(value) for key,value in td.items()}
    rl=[]
    for key,valuel in td.items():
        for com_right in itertools.combinations(valuel,count-1):
            com=(key,)+com_right
            label=True
            for i in range(1,count):
                main=com[i]
                test=com[:i]+com[i+1:]
                if not(all([t in tds[main] for t in test])):
                    label=False
                    break
            if label:
                rl.append(com)
    return rl