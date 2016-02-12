# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:37:19 2015

@author: yiyuezhuo
"""
import math
import collections

l=[i for i in range(1,1000)if i%3==0 or i%5==0]
print sum(l)

l=[1,2]
while l[-1]<4000000:
    l.append(l[-2]+l[-1])
l=l[:-1]
print sum([i for i in l if i%2==0])

s=600851475143
sl=[]
for i in range(2,10000):
    if all([i%j!=0 for j in range(2,int(math.sqrt(i))+1)]):
        sl.append(i)
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

#r=picktopick(s,sl)

def judge(n):
    s=str(n)
    s2=list(s)
    s2.reverse()
    s2=''.join(s2)
    return s==s2
'''
nl=[]
for i in range(100,1000):
    for j in range(100,1000):
        n=i*j
        if judge(n):
            nl.append(n)
'''
def simply(nl):
    #给出可以通过乘积得到nl中全部元素的最小集合,nl里不能有0
    rl=[picktopick(i,sl) for i in nl]
    listl=[term[1] for term in rl]
    #print listl
    keep={}
    for term in listl:
        cc=collections.Counter(term)
        for key in cc.keys():
            if keep.has_key(key):
                if cc[key]>keep[key]:
                    keep[key]=cc[key]
            else:
                keep[key]=cc[key]
    return keep
def counter_tend(dic):
    l=[]
    for key in dic.keys():
        l.extend(dic[key]*[key])
    return l
#print reduce(lambda x,y:x*y,counter_tend(simply(range(1,20))))
#print sum(range(11))**2-sum([i**2 for i in range(11)])
def prime_gen(n):
    kl=[2]
    test=3
    while len(kl)<n:
        #if all([test%i!=0 for i in kl]):
        label=True
        for prime  in kl:
            if test%prime==0:
                label=False;
                break;
        if label:
            kl.append(test)
        test+=1
    return kl
def times(l):
    return reduce(lambda x,y:x*y,l)
s='''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''
'''
tl=[int(i) for i in s if i!='\n']
rl=[]
for i in range(len(tl)-13):
    rl.append(times(tl[i:i+13]))
'''
'''
for i in range(1000):
    for j in range(i,1000):
        k=1000-i-j
        if not(i<j<k):
            continue
        if i**2+j**2==k**2:
            print i,j,k
'''
#200万那个上真筛法
def boult(big):
    l=range(big+1)
    for i in xrange(2,big):
        if l[i]!=None:
            for j in xrange(big//i-1):
                #print i,j
                l[i*(j+2)]=None
    return l
ss='''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
sl=ss.split('\n')
sm=[line.split(' ') for line in sl]
nm=[[int(word) for word in line]for line in sm]
def line_product_max(line):
    if len(line)<4:
        return -1
    else:
        pl=[]
        for i in range(len(line)-3):
            pl.append(times(line[i:i+4]))
        return max(pl)
def total(mat):
    m,n=len(mat),len(mat[0])
rl=[]
pf=[[(0,1),(0,2),(0,3)],[(1,0),(2,0),(3,0)],[(1,1),(2,2),(3,3)],
     [(1,-1),(2,-2),(3,-3)]]
for x in range(len(nm)):
    for y in range(len(nm[0])):
        for pp in pf:
            try:
                points=[(p[0]+x,p[1]+y) for p in [(0,0)]+pp]
                numbers=[nm[p[0]][p[1]] for p in points]
                r=times(numbers)
                rl.append(r)
            except IndexError:
                pass
def picktonumber(n,sl):
    r=picktopick(n,sl)[1]
    c=collections.Counter(r).values()
    cc=[i+1 for i in c]
    return  times(cc)
#rl=[picktonumber((1+i)*i/2,range(2,int(math.sqrt((1+i)*i/2))+1)) for i in range(10000)]
#for i in range():
s='''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''
l=[int(sl) for sl in s.split('\n')]
r=str(sum(l))[:10]
def Collatz(n):
    rl=[n]
    while True:
        if n==1:
            return rl
        else:
            if n%2==0:
                n=n/2
                rl.append(n)
            else:
                n=3*n+1
                rl.append(n)
def Coll(n,dic):#dic应至少有dic[1]=1
    if dic.has_key(n):
        return dic[n]
    else:
        if n%2==0:
            m=Coll(n/2,dic)
        else:
            m=Coll(n*3+1,dic)
        dic[n]=m+1
        return m+1
dic={1:1}
'''
for i in range(1000*1000,1,-1):
    Coll(i,dic)'''
def Lat(x,y,dic):
    if dic.has_key((x,y)):
        return dic[(x,y)]
    elif x==0 or y==0:
        dic[(x,y)]=0
        return 0
    else:
        a=Lat(x-1,y,dic)
        b=Lat(x,y-1,dic)
        dic[(x,y)]=a+b
        return a+b

def get_digit(n):
    return len(str(n))
def onedigit(n):
    #1-9
    dic={1:'one',2:'two',3:'three',4:'four',5:'five',
         6:'six',7:'seven',8:'eight',9:'nine'}
    return dic[n]
def twodigit(n):
    #10-99
    dic={10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',
         15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
         20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
         80:'eighty',90:'ninety'}
    if dic.has_key(n):
        return dic[n]
    else:
        return dic[n-n%10]+'-'+onedigit(n%10)
def threedigit(n):
    #100-999
    if n%100==0:
        return onedigit((n-n%100)/100)+' hundred'
    else:
        digit=get_digit(n%100)
        if digit==2:
            return onedigit((n-n%100)/100)+' hundred and '+twodigit(n%100)
        else:
            return onedigit((n-n%100)/100)+' hundred and '+onedigit(n%100)
def fourdigit(n):
    #1000
    assert n==1000
    return 'one thousand'
def number_to_str(n):
    digit=len(str(n))
    if digit==1:
        return onedigit(n)
    elif digit==2:
        return twodigit(n)
    elif digit==3:
        return threedigit(n)
    else:
        return fourdigit(n)
def custom_len(s):
    return sum([1 if i.isalpha() else 0 for i in s])
rl=[custom_len(number_to_str(i)) for i in range(1,1001)]
print sum(rl)
sm='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
nl=[[int(i) for i in line.split(' ')] for line in sm.split('\n')]
ll=[[75]]
for i in range(1,len(nl)):
    new_line=[ll[i-1][0]+nl[i][0]]
    for j in range(1,len(nl[i])-1):
        #print i,j
        v=nl[i][j]+max(ll[i-1][j-1],ll[i-1][j])
        new_line.append(v)
    last=len(nl[i])-1
    new_line.append(nl[i][last]+ll[i-1][last-1])
    ll.append(new_line)

def days_month(year,month):
    dic={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if month!=2:
        return dic[month]
    else:
        if (year%4==0 and year%100!=0) or year%400==0:
            return 29
        else:
            return 28
def days_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return 366
    else:
        return 365

def delta_days_month(montha,monthb):
    assert montha>monthb
    
import datetime
def sunday_q(date):
    s=datetime.datetime(1900,1,1)
    #d=datetime.timedelta(date,s)
    d=date-s
    return d.days%7==6
def gen_range():
    l=[]
    for year in range(1901,2001):
        for month in range(1,13):
            for day in range(1,32):
                try:
                    l.append(datetime.datetime(year,month,day))
                except ValueError:
                    pass
    return l
date_range=gen_range()
l=[]
for date in date_range:
    if date.day==1 and sunday_q(date):
        l.append(date)
print 'date_l',len(l)

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return fact(n-1)*n
    #return n if n==1 or n==0 else n*fact(n-1)
fact_store={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
def fact_quick(n):
    return fact_store[n]
    
def pickseq(n):
    _,l=picktopick(n,range(2,10000))
    return list(set(l))
def d(n):
    return sum(pickseq(n))
def pos(n):
    if n==1:
        return [(0,),(1,)]
    else:
        r=pos(n-1)
        ones=[(1,)+seq for seq in r]
        zeros=[(0,)+seq for seq in r]
        return ones+zeros
def pos2(counter):
    big_l=[1]
    for key,value in counter.items():
        temp_l=[key**i for i in range(0,value+1)]
        new_l=[]
        for old in big_l:
            new_l.extend([temp*old for temp in temp_l])
        big_l=new_l
    return big_l
    
def get_divisors(n):
    _,l=picktopick(n,range(2,int(math.sqrt(n))+1))
    if _!=1:
        l.append(_)
    c=collections.Counter(l)
    #r=[sum(l[j]*pl[i][j] for j in range(len(l))) for i in range(len(pl))]
    #return r
    r=pos2(c)
    return r
    
def d(n):
    l=get_divisors(n)
    return sum(l)-n
'''
l=[]
for n in range(2,10000):
    if d(n)!=n and d(d(n))==n:
        l.append(n)
'''
alpha_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dic={alpha_list[i]:i+1 for i in range(26)}
def score(name):
    return sum(alpha_dic[c] for c in list(name))

f=open('p022_names.txt','r')
s=f.read()
f.close()  
sl=[name[1:-1] for name in s.split(',')]
sl.sort()
r=sum(score(sl[i])*(i+1) for i in range(len(sl)))

import itertools

def abundant():
    return [i for i in range(2,28123) if d(i)>i]
def cl():
    l=set(range(1,28123))
    al=abundant()
    dl=set([sum(i) for i in itertools.product(al,al) if sum(i)<28123])
    return l-dl

def fib(n):
    F=[1,1]
    while True:
        if len(str(F[-1]))>=1000:
            return F
        F.append(F[-1]+F[-2])
def cycle(n,cut):
    l=[]
    numerator=1
    for i in range(cut):
        numerator*=10
        new=numerator//n
        l.append(new)
        numerator=numerator-new*n
    return l
    
def index_back(atom,l):
    l.reverse()
    t=l.index(atom)
    l.reverse()
    return len(l)-t-1
def index_map(atom,l):
    rl=[i for i in range(len(l)) if l[i]==atom]
    return rl
def cycle_cut(n,cut,testing=False):
    l=[]
    numerator=1
    nl=[]
    for i in range(cut):
        if numerator in nl:
            index=index_map(numerator,nl)[-1]
            #print testing
            if testing:
                print 'nl',nl
                print 'numerator',numerator
                print 'index',index
                print 'l',l
            
            return l[index:]
        nl.append(numerator)
        numerator*=10
        #nl.append(numerator)
        new=numerator//n
        l.append(new)
        numerator=numerator-new*n
    if testing:
                print 'nl',nl
                print 'numerator',numerator
                #print 'index',index
                print 'l',l

    return l
'''
l=[cycle_cut(i,1000) for i in range(2,1000)]
ll=[len(i) for i in l ]
ans=max(ll)'''
'''
pl=prime_gen(169)
big_pl=set(prime_gen(10000))#max- 104729
cut_max=max(big_pl)
cut=1000

rd={}
for b in pl:
    al=[p-b-1 for p in pl]
    for a in al:
        n=0
        for x in range(0,cut):
            f=x**2+a*x+b
            assert f<cut_max
            if f in big_pl:
                n+=1
            else:
                rd[(a,b)]=n
                break
                '''
def level_cal(n):
    head=((n-2)*2+1)**2+1
    interval=1+2*(n-2)
    first=head+interval
    last=first+(interval+1)*3
    #print head,interval,first,last
    return 2*(first+last)
def cum_cal(n):
    return 1+sum([level_cal(i) for i in range(2,(n-1)/2+1+1)])
'''
pm=itertools.product(range(2,101),range(2,101))
ps=set([x**y for x,y in pm])'''
#top=9**5*5
#rl=[i for i in range(2,top+1) if sum(int(j)**5 for j in str(i))==i]
#com_map={0:1,1:2,2:5,3:10,4:20,5:50,6:100,7:200}
#com_map_rev={value:key for key,value in com_map.items()}
def com(n,dic):
    cl=[1,2,5,10,20,50,100,200]
    if dic.has_key(n):
        return dic[n]
    else:
        al=[c for c in cl if n-c>=0]
        ans=set()
        for a in al:
            old=com(n-a,dic)
            at=set(tuple([i[j] if j!=com_map_rev[a] else i[j]+1 for j in range(8)]) for i in old)
            ans=ans|at
        dic[n]=ans
        return ans
#dic={0:set([(0,0,0,0,0,0,0,0)])}
#ans=com(200,dic)
        
# 4-2,4-1,3-2,3-1,
def pandigital(i,j,k):
    line=str(i)+str(j)+str(k)
    return len(line)==9 and set(line)==set('123456789')
    #return len(line)==9 and len(set(line))==9 
'''
ss=set()
sss=set()
for i in range(100,10000):
    for j in range(0,100):
        k=i*j
        if pandigital(i,j,k):
            ss.add(k)
            sss.add((i,j,k))'''
l=[]
for x in range(10,100):
    for y in range(x+1,100):
            uni=set(str(x))&set(str(y))
            if len(uni)!=0:
                u=list(uni)[0]
                xl=list(str(x))
                yl=list(str(y))
                xl.remove(u)
                yl.remove(u)
                xx=int(xl[0])
                yy=int(yl[0])
                if yy!=0 and abs(float(x)/y-float(xx)/yy)<1e-6:
                    l.append((x,y))
def cruious(n):
    return sum(fact(int(i)) for i in list(str(n)))
def circular(n):
    nl=[i for i in list(str(n))]
    nll=[nl]
    for i in range(len(nl)-1):
        ing=nll[-1][:]
        head=ing[0]
        del ing[0]
        ing.append(head)
        nll.append(ing)
    rl=[int(''.join(ll)) for ll in nll]
    return list(set(rl))
def circular_check(n,obj_set):
    #obj_set=set(obj_set)
    cl=circular(n)
    return all((c in obj_set) for c in cl)
def load_prime():
    import pickle
    f=open('prime_numbers','rb')
    obj=pickle.load(f)
    f.close()
    return obj
def palindromic_check(n):
    s=str(n)
    return all(s[i]==s[-i-1] for i in range(len(s)))
def binary(n):
    n=int(n)
    seq=[]
    while n>=2:
        seq.append(n%2)
        n=n//2
    seq.append(n)
    seq.reverse()
    s=''.join(str(s) for s in seq)
    return s
def truncatable_primes(n,given_set):
    s=str(n)
    sl=[int(''.join(s[i:])) for i in range(len(s))]
    sll=[int(''.join(s[:i])) for i in range(1,len(s))]
    ss=set(sl+sll)
    return all((i in given_set) for i in ss)
def sb(n):
    l=[str(n)]
    for i in range(2,10):
        ing=l[-1]
        l.append(ing+str(i*n))
    return [int(i) for i in l if len(i)<=9]


'''
l=[]
for i in range(1,5000000):
    if cruious(i)==i:
        l.append(i)'''