# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:04:41 2016

@author: yiyuezhuo

无论什么时候不忘我数据分析的老本行，这里要收集Project Euler原版的问题信息
与中文翻译站的信息。除了首页内容外还应该包括问题与翻译的字数，这是此次分析的
重点。
"""
import requests
import os
#import time
from bs4 import BeautifulSoup

header_s='''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8,en;q=0.6
Connection:keep-alive
Cookie:DYNSRV=lin105; keep_alive=863704%23PqEwAaQ5u2VobNlacNol3DBpcJf3IiA6; PHPSESSID=42a0460f8656babda467f9b76d04c163
Host:projecteuler.net
Referer:https://projecteuler.net/archives;page=4
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'''
headers={}
for line in header_s.split('\n'):
    print line
    index=line.index(':')
    key,value=line[:index],line[index:]
    headers[key]=value
del headers['Cookie']
cookies={'DYNSRV':'lin105','keep_alive':'863704%23PqEwAaQ5u2VobNlacNol3DBpcJf3IiA6','PHPSESSID':'42a0460f8656babda467f9b76d04c163'}

def projecteuler_archive_download(root='html/'):
    '''https://projecteuler.net/archives;page=2'''
    for i in range(1,12):
        print 'downloading',i
        url='https://projecteuler.net/archives;page='+str(i)
        #result=requests.get(url,headers=headers)
        result=requests.get(url,cookies=cookies)
        path=root+'projecteuler_archive_'+str(i)+'.html'
        f=open(path,'w')
        f.write(result.content)
        f.close()

def spirtzhang_download(root='html/'):
    '''http://pe.spiritzhang.com/index.php/2011-05-11-09-44-54?start=50'''
    for i in range(6):
        print 'downloading',i
        url='http://pe.spiritzhang.com/index.php/2011-05-11-09-44-54'
        params={'start':i*50}
        result=requests.get(url,params=params)
        path=root+'spirtzhang_'+str(i)+'.html'
        f=open(path,'w')
        f.write(result.content)
        f.close()

def projecteuler_problem_download(root='html/'):
    '''https://projecteuler.net/problem=536'''
    for i in range(1,537):
        print 'downloading',i
        url='https://projecteuler.net/problem='+str(i)
        result=requests.get(url)
        path=root+'projecteuler_problem_'+str(i)+'.html'
        f=open(path,'w')
        f.write(result.content)
        f.close()
        
class Query(object):
    def __init__(self,var_list=None,url_prefix='',url_suffix='',path_prefix='',
                 path_suffix='.html'):
        self.var_list=var_list
        self.url_prefix=url_prefix
        self.url_suffix=url_suffix
        self.path_prefix=path_prefix
        self.path_suffix=path_suffix
    def get_url(self,var):
        '''这个函数用于通过var_list里的一个值生成url,一般应当进行重写,
        不过默认情况可以用__init__里的字符串标记填充'''
        return self.url_prefix+var+self.url_suffix
    def get_path(self,var):
        '''这个函数用于通过var_list里的一个值生成path，如果当前path里
        已经有那个文件则不会重新下载,一般应当进行重写'''
        return self.path_prefix+var+self.path_suffix
    def report_downloading(self,var):
        print 'downloading',var
    def report_exists(self,var):
        print 'exists',var
    def do(self,over=False):
        for var in self.var_list:
            url=self.get_url(var)
            path=self.get_path(var)
            if not(over) and os.path.exists(path):
                self.report_exists(var)
                continue
            else:
                self.report_downloading(var)
                r=self.download(url,var)
                self.save(r,path)
    def download(self,url,var):
        '''具体控制如何download，接收url,var应该返回一个result对象,
        该方法一般应该重写'''
        return requests.get(url)
    def save(self,r,path):
        f=open(path,'w')
        f.write(r.content)
        f.close()
    def load(self,path):
        f=open(path,'r')
        s=f.read()
        f.close()
        return s
    def load_var(self,var):
        return self.load(self.get_path(var))
    def is_clear(self):
        return all([os.path.exists(self.get_path(var)) for var in self.var_list])
    def do_forever(self,itermax=10):
        for i in range(itermax):
            if self.is_clear():
                print 'clear'
                break
            try:
                self.do()
            except requests.ConnectionError,e:
                print e
    def to_obj(self,loads,var):
        '''将载入的loads转换成一个对象（列表/字典）,子类应当重写此方法'''
        return None
    def to_data(self):
        rl=[]
        for var in self.var_list:
            rl.append(self.to_obj(self.load_var(var),var))
        return rl
            
class Archive(Query):
    def __init__(self):
        Query.__init__(self)
        self.var_list=range(1,12)
    def get_url(self,var):
        return 'https://projecteuler.net/archives;page='+str(var)
    def get_path(self,var):
        root='html/'
        return root+'projecteuler_archive_'+str(var)+'.html'
    def download(self,url,var):
        return requests.get(url,cookies=cookies)
        
class Archive_CN(Query):
    def __init__(self):
        Query.__init__(self)
        self.var_list=range(6)
    def get_url(self,var):
        return 'http://pe.spiritzhang.com/index.php/2011-05-11-09-44-54'
    def get_path(self,var):
        root='html/'
        return root+'spirtzhang_'+str(var)+'.html'
    def download(self,url,var):
        params={'start':var*50}
        return requests.get(url,params=params)
    def to_obj(self,loads,var):
        soup=BeautifulSoup(loads)
        tr=soup.findAll(attrs={'class':'sectiontableheader','align':"right"})[0].parent
        trp=tr
        rl=[]
        while True:
            trp=trp.nextSibling.nextSibling
            tds=trp.findAll('td')
            if len(tds)==4:#valid
                ID=tds[0].text.strip()
                des=tds[1].text.strip()
                aut=tds[2].text.strip()
                hit=tds[3].text.strip()
                href=trp.findAll('a')[0].attrs['href']
                obj={'id':int(ID),'des':des,'aut':aut,'hit':hit,'href':href}
                rl.append(obj)
            else:
                break
        return rl
        
        
class Problem(Query):
    def __init__(self):
        Query.__init__(self)
        self.var_list=range(1,537)
    def get_url(self,var):
        return 'https://projecteuler.net/problem='+str(var)
    def get_path(self,var):
        root='html/'
        return root+'projecteuler_problem_'+str(var)+'.html'
    def to_obj(self,loads,var):
        soup=BeautifulSoup(loads)
        div=soup.findAll(attrs={'id':'problem_info'})[0]
        problem_info=div.findAll('span')[0].text
        time,solve,diff=problem_info.split(';')
        solve=solve[solve.index('by')+2:].strip()
        diff=diff[diff.index(':')+1:-1].strip()
        div=soup.findAll(attrs={'class':'problem_content'})[0]
        content=div.text
        obj={'id':var,'time':time,'solve':solve,'diff':diff,'content':content,
             'length':len(content)}
        return obj
        
class Problem_CN(Query):
    def __init__(self,id_to_href_map):
        Query.__init__(self)
        self.var_list=range(1,263)
        self.id_to_href_map=id_to_href_map
    def get_url(self,var):
        href=self.id_to_href_map[str(var)]
        return 'http://pe.spiritzhang.com'+href
    def get_path(self,var):
        root='html/'
        return root+'spiritzhang_problem_'+str(var)+'.html'
    def to_obj(self,loads,var):
        soup=BeautifulSoup(loads)
        div=soup.findAll(attrs={'class':'article-content'})[0]
        return {'id':var,'text':div.text,'length':len(div.text)}
        
def integration():
    def by_id(l):
        return {obj['id']:obj for obj in l}
    problem_d=by_id(problem.to_data())
    problem_cn_d=by_id(problem_cn.to_data())
    archive_cn_d=by_id(sum(archive_cn.to_data(),[]))
    rl=[]
    for i in range(1,263):
        pd=problem_d[i]
        pcd=problem_cn_d[i]
        acd=archive_cn_d[i]
        hit=int(acd['hit'])
        des_len=len(acd['des'])
        diff=int(pd['diff'])
        content=pd['length']
        t_content=pcd['length']
        solve=int(pd['solve'])
        obj={'id':pd['id'],'hit':hit,'des_len':des_len,'diff':diff,
        'content':content,'t_content':t_content,'solve':solve}
        rl.append(obj)
    return rl
        
        
    
    

archive=Archive()
archive_cn=Archive_CN()
problem=Problem()

dl=archive_cn.to_data()
id_to_href_map={d['id']:d['href'] for d in sum(dl,[])}

problem_cn=Problem_CN(id_to_href_map)

#bl=integration()
#dt=pd.DataFrame(bl)
#dt.index=dt['id']

#problem.do_forever()
#problem.do()
#html=archive_cn.load_var(archive_cn.var_list[0])
#soup=BeautifulSoup(html)

#html=problem_cn.load_var(problem_cn.var_list[0])
#soup=BeautifulSoup(html)

#html=problem.load_var(problem.var_list[0])
#soup=BeautifulSoup(html)