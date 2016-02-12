# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 21:42:44 2016

@author: yiyuezhuo
"""

import math
import itertools
from factor_tool import pickmap
from collections import Counter

n=120
l=[]

for x in range(1,n/2+1):
    for y in range(1,x+1):
        p=n
        if p**2-2*p*x-2*p*y+2*x*y==0:
            l.append((x,y,n-x-y))
            
def p39_get(p):
    l=[]
    for x in range(1,p/2+1):
        for y in range(1,x+1):
            if p**2-2*p*x-2*p*y+2*x*y==0:
                l.append((x,y,p-x-y))
    return l
    
def p39():
    l=[p39_get(i) for i in range(1,1001)]
    return max(range(len(l)),key=lambda x:len(l[x]))
    
def p40_s(n):
    '''
    s=''
    for i in range(1,n+1):
        s+=str(i)
    return s
    '''
    return ''.join([str(i) for i in range(0,n)])
    
def p40():
    d=p40_s(1000000)
    dl=[int(d[10**i]) for i in range(7)]
    return reduce(lambda x,y:x*y,dl,1)
    
def get_prime_by_cache():
    import pickle
    f=open('prime_numbers','rb')
    obj=pickle.load(f)
    f.close()
    return obj
    
def p41_quick_prime_judge(n,prime_l,cut=10000):
    for i in range(cut):
        tr=prime_l[i]
        if n%tr==0:
            if n==tr:
                return True
            else:
                return False
    return True

def p41(prime_l,seq='9876543210',digit=10):
    for n in itertools.permutations(seq,digit):
        n=int(''.join(n))
        if p41_quick_prime_judge(n,prime_l):
            return n
#Tp41(prime_l,seq='7654321',digit=7)

def p41_move(prime_l,moved=3628800-100,seq='9876543210'):
    it=itertools.permutations(seq,len(seq))
    for i in range(moved):
        it.next()
    for n in it:
        n=int(''.join(n))
        if p41_quick_prime_judge(n,prime_l):
            return n
    
    
def p42_parse():
    f=open('p042_words.txt','r')
    s=f.read()
    f.close()
    s=''.join(s.split('\n'))
    return [w[1:-1] for w in s.split(',')]

def p42_word_value(word):
    seq='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sum([seq.index(a) for a in word])+len(word)
    
def p42_is_triangle_number(n):
    #t_n=(1/2)*(n(n+1))
    #exist n 0.5n+0.5n**2=m  0.5x**2+0.5x-n
    delta=0.25+2*n
    if delta<0:
        return False
    else:
        x1=-0.5+math.sqrt(delta)
        x2=-0.5-math.sqrt(delta)
        return x1==int(x1) or x2==int(x2)
    
    
def p42():
    value_l=map(p42_word_value,p42_parse())
    return len(filter(p42_is_triangle_number,value_l))
    
class Node(object):
    def __init__(self,parent=None,move=None,value=None):
        self.parent=parent
        if parent==None:
            self.parent=None
            self.move=None
            self.prohibit=value
            self.value=str(value)
        else:
            self.parent=parent
            self.move=move
            self.prohibit=move+parent.prohibit
            self.value=move+parent.value[:2]
        self.child=[]
    def expand(self,factor):
        for i in range(10):
            if not(str(i) in self.prohibit):
                new=int(i+self.value[:2])
                if new % factor==0:
                    self.child.append(Node(parent=self,move=str(i)))

def p43_roots():
    rl=[]
    for it in itertools.permutations('0123456789',3):
        n=int(''.join(it))
        if n % 17==0:
            rl.append(n)
    return rl
    
class Node2(object):
    def __init__(self,parent,value,move_list,factor_stack):
        #这里的value,move都默认是字符串,但factor是数值栈
        self.value=value
        self.move_list=move_list
        self.factor_stack=factor_stack[:]
        self.child=[]
    def expand(self):
        factor_stack=self.factor_stack[:]
        if len(factor_stack)==0:
            return self.child #[]
        factor=factor_stack[-1]
        for move in self.move_list:
            if int(move+self.value[:2]) % factor==0:
                move_list=self.move_list[:]
                move_list.remove(move)
                node=Node2(self,move+self.value[:2],move_list,factor_stack[:-1])
                self.child.append(node)
        return self.child # return whether expand a node
    def expand_all(self):
        level=self.expand()
        while len(level)!=0:
            l=[]
            level_l=[node.expand() for node in level]
            for ll in level_l:
                l.extend(ll)
            level=l
    def back(self):
        if len(self.child)==0 and len(self.factor_stack)==0:
            return [self.move_list[0]+self.value]
        else:
            rl=[]
            ll=[[unit+self.value[-1] for unit in child.back()] for child in self.child]
            for l in ll:
                rl.extend(l)
            return rl
    def print_tree(self,depth=0):
        print ' '*depth+self.value
        for child in self.child:
            child.print_tree(depth=depth+1)
                


def p43():
    #root_l=[Node(value=n) for n in p43_roots()]
    rl=[]
    root_l=[]
    for value in [str(number) for number in p43_roots()]:
        move_list=list('0123456789')
        for s in value:
            move_list.remove(s)
        factor_stack=[2,3,5,7,11,13]
        root=Node2(None,value,move_list,factor_stack)
        root.expand_all()
        rl.extend(root.back())
        root_l.append(root)
    return sum(map(len,rl))
    #return root_l
    
#def p44_seq():
'''
p44可以试图找到这样一个“基数”，该基数是五边形数序列中的一个，我们试图找到另一个
（更大的）五边形数，使其和也是五边形数。这样反过来看也就是那个新数与第二个数
之差也是个五边形数（第一个数），而我们的目的正是使得这样的差最小化，换而言之
就是使基数最小化。为了做到这一点，我们按顺序从五边形数序列中搜索，判定其是否能满足
与另一个（更大的，由对称性）五边形数的性质，这样一旦发现就可以停机并得到该基数就是
我们所要求的D的结论。而为了在有限步内做出这样的判定，我们可以注意到五边形数临数之间
的间距越来越大，当基数比间距还小时，当然之后的基数永远不可能合成另一个基数，如果
的确做到了这一步，则可以判定该数不满足此性质，故而满足有限性条件。
P_n=n(3n-1)/2 = 1.5n^2-0.5n
P_{n-1}=(n-1)(3n-4)/2 = 1.5n^2-3.5n+2
P_n-P_{n-1}=3n-2

3n-2 < try_number

完全搞错了。。这样不吼
'''
def p44_match(n,pentagonal_list,pentagonal_set):
    #这个n表示的是第n个五边形数而不是n这个数
    base=pentagonal_list[n]
    for i in range(n+1,int((base+2)/3.0)+100):
        second=pentagonal_list[i]
        if ((base+second) in pentagonal_set) and (base+2*second in pentagonal_set):
            print 'base',base,'second',second,'third',base+second,'fourth',base+2*second
            return True
    return False
    
def p44(limit=1000000):
    pentagonal_list=[(3*i-1)*i/2 for i in range(1,limit)]
    pentagonal_set=set(pentagonal_list)
    for i in range(limit):
        if p44_match(i,pentagonal_list,pentagonal_set):
            return pentagonal_list[i]
            
def p44_force(limit=1000):
    pentagonal_list=[(3*i-1)*i/2 for i in range(1,limit)]
    pentagonal_set=set(pentagonal_list)
    for i in range(limit/2):
        for j in range(limit/2):
            second=pentagonal_list[i]
            third=pentagonal_list[j]
            first=third-second
            fourth=second+third
            if first in pentagonal_set and fourth in pentagonal_set:
                print 'first',first,'second',second,'third',third,'fourth',fourth
                return first
#first 5482660 second 1560090 third 7042750 fourth 8602840
#true ans is 5482660
def p45(limit=100000):
    Triangle=[n*(n+1)/2 for n in range(limit)]
    Pentagonal=[n*(3*n-1)/2 for n in range(limit)]
    Hexagonal=[n*(2*n-1) for n in range(limit)]
    Triangle_s=set(Triangle)
    Pentagonal_s=set(Pentagonal)
    Hexagonal_s=set(Hexagonal)
    rs=Triangle_s & Pentagonal_s & Hexagonal_s
    return rs
    
def p46_decompose_(n,prime_l):
    # n is a odd number
    for i in prime_l:
        if n<i:
            break
        res=n-i
        right=math.sqrt(res/2)
        if right==int(right):
            return i,right
    return None
    
def p46_decompose(n,prime_set):
    for i in range(int(math.sqrt(n/2))+1):
        test=n-i*i*2
        if test in prime_set:
            return test,i
    return None
    
def p46_(prime_l,limit=10000):
    for i in range(limit):
        n=i*2+1
        r=p46_decompose(n,prime_l)
        if r==None:
            return r
            
def p46(prime_s,limit=1000000):
    for i in range(1,limit):
        n=i*2+1
        if p46_decompose(n,prime_s)==None:
            return n
#p46(prime_s)
#5777
def p47(n,prime_l,limit=100000):
    keep_l=[]
    for i in range(3,limit):
        new=set(tuple(pickmap(i,prime_l).items()))
        if len(new)==n:
            new_keep_l=[new]
            for keep in keep_l[::-1]:
                if len(keep & new)==0:
                    new_keep_l.append(keep)
                else:
                    break
            new_keep_l.reverse()
            keep_l=new_keep_l
        else:
            keep_l=[]
        if len(keep_l)==n:
            return i-n+1
#p47(4,prime_l,limit=1000000)
#134043

def p48():
    return str(sum([i**i for i in range(1,1001)]))[-10:]
    
def p49_extend(n):
    raw=str(n)
    rl=[]
    for seq in itertools.permutations(raw,len(raw)):
        rl.append(int(''.join(seq)))
    rl=list(set(rl))
    rl.remove(n)
    return rl

def p49(prime_s):
    rl=[]
    for i in range(1000,10000):
        ext=p49_extend(i)
        for ex in ext:
            first=min(ex,i)
            second=max(ex,i)
            third=2*second-first
            if len(str(third))==4 and set(str(third))==set(str(second)):
                rl.append((first,second,third))
    rl=[com for com in rl if all([i in prime_s for i in com])]
    return rl
#296962999629
    
def _p50(cut,prime_l,prime_s):
    ans_l=[]
    for base in range(1000):
        psl=[]
        ps=0
        for p in prime_l[base:]:
            ps+=p
            if ps in prime_s:
                psl.append(ps)
        for i in range(len(psl)):
            ps=psl[i]
            if len(str(ps))>cut:
                ans_l.append(psl[i-1])
    return ans_l
    
def p50(cut,prime_l,prime_s):
    sl=[]
    dl=[]
    for i in range(1500):
        for j in range(i+1,1500):
            s=sum(prime_l[i:j])
            if len(str(s))==cut and s in prime_s:#100,0000
                sl.append(s)
                dl.append(abs(i-j))
    return sl[dl.index(max(dl))]
    #return rl
#p50(6,prime_l,prime_s)
#997651
    
def p51(hit,change_digit,space_digit,prime_l,prime_s):
    '''
    尼玛上不了网，这题大概就是找住一个这样的相同位数的素数族，它们可以通过变换
    相同位上的数为不同的数（但各位上的数是相同的）来生成不同的素数。
    当然以Project Euler的尿性你要提交的是这个族中最小的那个。貌似是要求包含8个
    元素的族？之前貌似给出了2个与多少个的例子。
    麻烦要在多少位数里搜索,改变多少位这些都是不确定的，比较坑
    '''
    for prime in prime_l:
        if len(str(prime))==space_digit:
            base=list(str(prime))
            for com in itertools.combinations(range(space_digit),change_digit):
                score=0
                for i in range(10):
                    new=base[:]
                    #print new
                    for digit in com:
                        new[digit]=str(i)
                    new=int(''.join(new))
                    #print new
                    if new in prime_s and len(str(new))==space_digit:
                        score+=1
                if score==hit:
                    return base,com
#p51(8,3,6,prime_l,prime_s)
#(['1', '2', '0', '3', '8', '3'], (0, 2, 4))
#121313
                    
def p52(itermax=1000000):
    for i in range(1,itermax):
        digit=len(str(i))
        base=set(str(i))
        rl=[]
        for j in range(1,7):
            b2=str(i*j)
            if len(b2)==digit and set(b2)==base:
                rl.append(True)
            else:
                rl.append(False)
                break
        if all(rl):
            return i
#p52()
#142852
def p53_fact(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
'''
def p53_com(r):
    n=10
    n_up=p53_fact(n)
    n_down=p53_fact(n-r)
    return n_up/(p53_fact(r)*n_down)
'''
def p53_com(n,r):
    #r=10
    return p53_fact(n)/(p53_fact(r)*p53_fact(n-r))
            
def _p53():
    s=0
    for n in range(1,101):
        if p53_com(n)>=1000000:
            s+=1
    return s
#78
def p53():
    s=0
    for n in range(1,101):
        for r in range(0,n+1):
            if p53_com(n,r)>=1000000:
                s+=1
    return s
#4075


            
    
'''
这题的正确做法应该是用素数列中的每个单独跑一趟，这样避免大因子分解的时间浪费
'''

'''
root_l=p43()
root=root_l[0]
root.print_tree()
'''
#rl=p43()     

#constrain
'''
x**2+y**2=z**2
x+y+z=p

x**2+y**2=(p-x-y)**2
x**2+y**2=p**2+x**2+y**2-2px-2py+2xy
0=p**2-2px-2py+2xy'''