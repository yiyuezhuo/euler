# 欧拉计划相关

## 代码


这次更新时题只做到了第64题（60,61,62暂且没做，讨厌数论风的），并没有什么用。然后我突然想看看欧拉计划中文翻译站的各条目的点击次数的关系。所以我收集两个
网站（Project Euler与欧拉计划翻译站）数据做了回归。结果看下面


爬虫代码放在 `data_craw.py` 里，要用要进行一些小修改。回归代码放在 `data_analyse.py` 里。

`data_craw.py` 提供的 `integration` 函数可以生成一个字典列表，其中元素有以下key

* `content` 英文题目文本长度
* `des_len` 中文描述长度
* `diff` 困难度评分
* `hit` 中文翻译点击数
* `id` 题目id
* `solve` 原版被求解成功次数
* `t_content` 中文翻译题目文本长度

## 结果


	mod=smf.ols('hit~t_content+diff+solve+id',data=dt)
	res=mod.fit()
	print res.summary()

								OLS Regression Results                            
	==============================================================================
	Dep. Variable:                    hit   R-squared:                       0.893
	Model:                            OLS   Adj. R-squared:                  0.892
	Method:                 Least Squares   F-statistic:                     537.6
	Date:                Sat, 13 Feb 2016   Prob (F-statistic):          1.61e-123
	Time:                        00:29:06   Log-Likelihood:                -1954.0
	No. Observations:                 262   AIC:                             3918.
	Df Residuals:                     257   BIC:                             3936.
	Df Model:                           4                                         
	Covariance Type:            nonrobust                                         
	==============================================================================
					 coef    std err          t      P>|t|      [95.0% Conf. Int.]
	------------------------------------------------------------------------------
	Intercept   1673.1256     74.930     22.329      0.000      1525.571  1820.680
	t_content      0.1003      0.075      1.344      0.180        -0.047     0.247
	diff           3.6178      2.112      1.713      0.088        -0.541     7.776
	solve          0.0145      0.000     29.606      0.000         0.014     0.015
	id            -6.1855      0.756     -8.186      0.000        -7.673    -4.698
	==============================================================================
	Omnibus:                      263.110   Durbin-Watson:                   1.162
	Prob(Omnibus):                  0.000   Jarque-Bera (JB):            20553.351
	Skew:                           3.654   Prob(JB):                         0.00
	Kurtosis:                      45.771   Cond. No.                     2.05e+05
	==============================================================================

	Warnings:
	[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
	[2] The condition number is large, 2.05e+05. This might indicate that there are
	strong multicollinearity or other numerical problems.
	
用id控制观察不到的随id变化的趋势（如新鲜感），我们可以看到一个问题越难，则点击相应翻译的人越多
一个问题翻译出来后文本越长，则点击的越多（然而并不显著）。而点击的当然随id增长而下降。solve的正效应则
体现了一种平均的点击效应。