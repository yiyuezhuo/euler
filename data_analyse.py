# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:20:19 2016

@author: yiyuezhuo
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from data_craw import integration
import matplotlib.pyplot as plt
#from scipy.optimize import leastsq
import fit_tool

plt.style.use('ggplot')


data_file_name='data.csv'

import os
if os.path.isfile(data_file_name):
    print('Load {} from cache'.format(data_file_name))
    df=pd.read_csv(data_file_name)
else:
    print('The cache is not established. Trying to create it from data_craw.py script')
    bl=integration()
    df=pd.DataFrame(bl)
    df.index=df['id']
    df.to_csv(data_file_name)



'''
content 英文题目文本长度
des_len 中文描述长度
diff 困难度评分
hit 中文翻译点击数
id 题目id
solve 原版被求解成功次数
t_content 中文翻译题目文本长度
'''


mod=smf.ols('hit~t_content+diff+solve+id+np.square(id)',data=df)
res2=mod.fit()
print(res2.summary())

def to_latex(summary, width_scale=0.5, col_scale=0.5, 
             print_only=True, center = True):
    header = '\\scalebox{{{}}}[{}]{{'.format(width_scale,col_scale)
    tail = '}'
    latex_list = []
    for table in summary.tables:
        latex = table.as_latex_tabular(center=False).replace('_','\\_')
        latex_list.append('\n'.join([header,latex,tail]))
    latex = '\n'.join(latex_list)
    if center:
        latex = '\n'.join([r'\begin{center}', latex, r'\end{center}'])
    if print_only:
        print(latex)
    else:
        return latex

'''
这里考察难度（变化）对当期题目和下期题目的中文翻译查询量（变化）的影响，
根据理论（常识），对于一个困难的的题目，可能因为以为自己不理解而
去查看中文翻译，但如果一个题真的十分困难，可能会使一部分人不会继续做下去，
这就体现在两种差分对齐方式上的不同行为，下面将进行估计
'''
'''当期差分，考察直接影响'''
def test(dt):
    diff=dt[['diff']].diff()
    hit=dt[['hit']].diff()
    diff=diff.applymap(lambda x:x if x>=0 else x/10.0)
    ddt=diff.join(hit)
    ddt['id']=dt['id']
    mod=smf.ols('hit~diff',data=ddt)
    res=mod.fit()
    print(res.summary())
'''
def exp_fit(x,y,p0=(1.0,1.0,1.0)):
    #x,y, are vector formal y=a*exp(b*x)+c
    def peval(x,p):
        a,b,c=p
        return a*np.exp(b*x)+c
    def residuals(p,y,x):
        return y-peval(x,p)
    plsq=leastsq(residuals,p0,args=(y,x))
    return plsq
'''
dfs=df.sort_values(by='solve',ascending=False)
dfs.index=range(len(dfs.index))
x=dfs.index.tolist()
y=dfs['solve'].tolist()
mod=fit_tool.ExponModel(y,x)
res=mod.fit()
res.summary()
res.plot()