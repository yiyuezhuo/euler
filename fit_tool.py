# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 21:05:25 2016

@author: yiyuezhuo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import itertools

plt.style.use('ggplot')



class Model(object):
    def __init__(self,endog,exog):
        self.endog=np.array(endog)
        self.exog=np.array(exog)
    def _fit(self,p0=None):
        def residuals(p,y,x):
            return y-self.peval(x,p)
        params=leastsq(residuals,p0,args=(self.endog,self.exog))[0]
        fit_result=FitResult(self,params=params)
        return fit_result
    def fit(self,p0=None):
        if p0!=None:
            return self._fit(p0=p0)
        else: # guess mode
            arity=len(self.__class__.params)
            ava=[]
            for p in itertools.product(*[[-1.0,1.0]]*arity):
                ava.append(self._fit(p0=p))
            tl=[(res,error2) for res,error2 in [(res,res.error2()) for res in ava] if not np.isnan(error2)]
            if len(tl)==0:
                return FitResult(self,succ=False)
            else:
                return min(tl,key=lambda t:t[1])[0]
    def peval(self,x,p):
        raise NotImplemented
        

class ExponModel(Model):
    params=('a','b','c')
    formula='y=a*exp(b*x)+c'
    def peval(self,x,p):
        a,b,c=p
        return a*np.exp(b*x)+c
        
class LinearModel(Model):
    params=('k','b')
    formula='y=k*x+b'
    def peval(self,x,p):
        k,b=p
        return k*x+b
        
class RecipModel(Model):
    params=('a','b','c')
    formula='y=a/(x+b)+c'
    def peval(self,x,p):
        a,b,c=p
        return a/(x+b)+c
    
def check(key,message='check fail'):
    def _check(method):
        def __check(self,*args,**kwargs):
            if getattr(self,key):
                return method(self,*args,**kwargs)
            else:
                print message
        return __check
    return _check

class FitResult(object):
    def __init__(self,model,params=None,succ=True):
        self.model=model
        self.params=params
        self.succ=succ
    def predict(self,exog):
        return self.model.peval(exog,self.params)
    def error2(self):
        return np.sum((self.model.endog-self.predict(self.model.exog))**2)
    @check('succ',message='fit fail')
    def summary(self):
        error2=self.error2()
        print 'Curve Fit Model'
        print '==================='
        print self.model.__class__.formula
        #print ' '.join(itertools.chain(*zip(self.model.__class__.params,self.params)))
        keys=self.model.__class__.params
        values=map(str,self.params)
        print ' '.join(itertools.chain(*zip(keys,values)))
        print 'error2',error2
    @check('succ',message='fit fail')
    def plot(self):
        plt.plot(self.model.exog,self.model.endog)
        plt.plot(self.model.exog,self.predict(self.model.exog))
        plt.legend(['Origin','Fit'])
        plt.show()
        
def fit(x,y,model='linear',p0=None,test_all=False):
    model_mapping={'linear':LinearModel,'expon':ExponModel,
                   'recip':RecipModel}
    if not test_all:
        mod=model_mapping[model](y,x)
        res=mod.fit(p0=p0)
        res.summary()
        res.plot()
    else:
        for model in model_mapping.keys():
            fit(x,y,model=model,p0=p0,test_all=False)
        
if __name__=='__main__':
    x=np.linspace(1,10,1000)
    y=2*np.exp(-x)
    mod=ExponModel(y,x)
    res=mod.fit()
    res.summary()
    res.plot()