# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:17:16 2016

@author: yiyuezhuo
"""
from collections import Counter
from itertools import combinations

suits='''HCSD'''
p54_order='2,3,4,5,6,7,8,9,T,J,Q,K,A'.split(',')
p54_rank_map={p54_order[i]:i for i in range(len(p54_order))}
types=['High Card','One Pair','Two Pairs','Three of a Kind',
       'Straight','Flush','Full House','Four of a Kind',
       'Straight','Royal Flush']
score_map={types[i]:i for i in range(len(types))}

def rank_compare(rank):
    return p54_rank_map[rank]


class Cards(list):
    '''该类应该同时表示任意张牌的情形,使得子序列可以统一处理'''
    def __init__(self,hand):
        if type(hand)==type(""):
            hand=hand.split(' ')
        '''hand=['8C', 'TS', 'KC', '9H', '4S']'''
        list.__init__(self,hand)
        #print hand
        self.rank=[card[0] for card in hand]
        self.suit=[card[1] for card in hand]
    def is_consecutive(self):
        if len(self)!=5:
            return False
        rank=self.rank
        rank_value=[p54_rank_map[r] for r in rank]
        m=min(rank_value)
        if m>8:
            return False
        return all([p54_order[m+i] in set(rank) for i in range(1,5)])
    def is_same_suit(self):
        return len(set(self.suit))==1
    def is_same_rank(self):
        return len(set(self.rank))==1
    def subs(self,size=None):
        '''拥有的所有牌的组合，包含其本身'''
        if size==None:
            n=len(self)
            #return sum([list(combinations(self),i) for i in range(1,n+1)],[])
            sl=sum([list(combinations(self,i)) for i in range(1,n+1)],[])
            #return [Cards(ss) for ss in sl]
        else:
            sl=list(combinations(self,size))
        return [Cards(ss) for ss in sl]
        
class Hand(Cards):
    '''该类抽象作为5张牌时的特殊判定方法'''
    def __init__(self,hand):
        Cards.__init__(self,hand)
        self.horse=None#同级时用于比较的序列
    def judge(self):
        '''返回自己属于哪种类型的优先级'''
        if self.is_Royal_Flush():
            return 'Royal Flush'
        elif self.is_Straight_Flush():
            return 'Straight Flush'
        elif self.is_Four_of_a_Kind():
            return 'Four of a Kind'
        elif self.is_Full_House():
            return 'Full House'
        elif self.is_Flush():
            return 'Flush'
        elif self.is_Straight():
            return 'Straight'
        elif self.is_Three_of_a_Kind():
            return 'Three of a Kind'
        elif self.is_Two_Pairs():
            return 'Two Pairs'
        elif self.is_One_Pair():
            return 'One Pair'
        else:
            return 'High Card'
    def big_than_to(self,hand):
        '''比较自己与另一个Hand对象谁大,因为它说了不可能相同所以False就是小于'''
        self_score=score_map[self.judge()]
        other_score=score_map[hand.judge()]
        if self_score>other_score:
            return True
        elif self_score<other_score:
            return False
        else:
            self_score=self.score()
            other_score=hand.score()
            for i in range(len(self_score)):
                x=rank_compare(self_score[i])
                y=rank_compare(other_score[i])
                if x>y:
                    return True
                elif x<y:
                    return False
    def is_Royal_Flush(self):
        return set(self.rank)==set('TJQKA') and self.is_same_suit()
    def is_Straight_Flush(self):
        return self.is_consecutive() and self.is_same_suit()
    def is_Four_of_a_Kind(self):
        tl=[]
        for sub in self.subs(size=4):
            if sub.is_same_rank():
                tl.append(sub)
        if len(tl)!=0:
            self.horse=[tl[0][0][0],list(set(self.rank)-set(tl[0][0][0]))[0]]
            return True
        return False
    def is_Full_House(self):
        #return self.is_Three_of_a_Kind() and self.is_One_Pair()
        tl=[]
        for sub in self.subs(size=3):
            if sub.is_same_rank():
                if len(set(self.rank)-set(sub.rank))==1:
                    tl.append(sub)
        if len(tl)>=1:
            self.horse=[tl[0][0][0],list(set(self.rank)-set(tl[0][0][0]))[0]]
            return True
        return False
    def is_Flush(self):
        return self.is_same_suit()
    def is_Straight(self):
        return self.is_consecutive()
    def is_Three_of_a_Kind(self):
        tl=[]
        for sub in self.subs(size=3):
            if sub.is_same_rank():
                tl.append(sub)
        if len(tl)!=0:
            m=min(set(self.rank)-set(tl[0][0][0]),key=rank_compare)
            M=max(set(self.rank)-set(tl[0][0][0]),key=rank_compare)
            self.horse=[tl[0][0][0],M,m]
            return True
        return False
    def is_Two_Pairs(self):
        tl=[]
        for sub in self.subs(size=2):
            if sub.is_same_rank():
                tl.append(sub)
        if len(tl)>=2:
            m=min(tl[0][0][0],tl[1][0][0],key=rank_compare)
            M=max(tl[0][0][0],tl[1][0][0],key=rank_compare)
            single=list(set(self.rank)-set([m,M]))[0]
            self.horse=[M,m,single]
            return True
        else:
            return False
    def is_One_Pair(self):
        tl=[]
        for sub in self.subs(size=2):
            if sub.is_same_rank():
                tl.append(sub)
        if len(tl)>=1:
            pair=tl[0][0][0]
            surplus=sorted(list(set(self.rank)-set(pair)),key=rank_compare,reverse=True)
            self.horse=[pair]+surplus
            return True
        else:
            return False
    def score(self):
        '''对不同类型的内部优先级做特殊处理,返回比照列表
        其中Four of a Kind,Full House,Three of a Kind,
        Two Pairs,One Pairs不能使用缺省的策略'''
        if self.horse!=None:
            return self.horse
        else:
            return sorted(self.rank,key=rank_compare,reverse=True)
            
        
        
def p54_load(fname='p054_poker.txt'):
    f=open(fname,'r')
    s=f.read()
    f.close()
    sl=[]
    for ss in s.split('\n')[:-1]:
        sss=ss.split()
        sl.append((sss[:5],sss[5:]))
    return sl
    
def p54(fname='p054_poker.txt'):
    sl=p54_load(fname=fname)
    return sum([Hand(first).big_than_to(Hand(second)) for first,second in sl])
    
def debt(first,second):
    first=Hand(first)
    second=Hand(second)
    print ''
    print 'first',sorted(first,key=lambda x:p54_rank_map[x[0]]),'second',sorted(second,key=lambda x:p54_rank_map[x[0]])
    print 'first judge: ',first.judge(),first.horse,'|','second judge: ',second.judge(),second.horse
    print 'player1 win' if first.big_than_to(second) else 'player2 wins'

def test():
    print 'hit',p54(fname="p054_poker_test.txt")
    sl=p54_load(fname='p054_poker_test.txt')
    for first,second in sl:
        debt(first,second)
        
def test2():
    sl=p54_load()
    for first,second in sl:
        s=raw_input('')
        if s!='':
            break
        debt(first,second)

def test3():
    '''观测judge的频率审查相关异常'''
    sl=p54_load()
    hands=[]
    for first,second in sl:
        first=Hand(first)
        second=Hand(second)
        hands.extend([first,second])
    return Counter([hand.judge() for hand in hands])
    
def test4():
    '''应该打印出反着的优先级'''
    hands=['TH JH QH KH AH','2H 3H 4H 5H 6H','2H 2C 2S 2D 6H',
           '2H 2C 2S 6H 6C','2H 4H 6H 8H TH','2H 3H 4H 5H 6S',
           '2H 2C 2S 6H 8S','2H 2C 3H 3C 5H','2H 2C 5H 8S 9S',
           '2H 4C 6C 8H 9S']
    for hand in hands:
        hand=Hand(hand)
        print hand,hand.judge(),hand.horse