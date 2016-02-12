# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:20:19 2016

@author: yiyuezhuo
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from data_craw import integration

bl=integration()
dt=pd.DataFrame(bl)
dt.index=dt['id']
'''
content 英文题目文本长度
des_len 中文描述长度
diff 困难度评分
hit 中文翻译点击数
id 题目id
solve 原版被求解成功次数
t_content 中文翻译题目文本长度
'''

mod=smf.ols('hit~t_content+diff+solve+id,data=dt')
res=mod.fit()
print res.summary()