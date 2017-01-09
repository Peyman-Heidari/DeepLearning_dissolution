# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:43:05 2016

@author: mggm6
"""
import pandas as pd
import numpy as np


def xTransform(xVars):
    if type(xVars)!=type(pd.DataFrame()):
        raise TypeError("xVars must be a dataframe!!!")
    functionNames=['x','x^2','x^3','x^4','10^x','10^-x','x^-1','log10(x)','ln(x)','x^0.5','x^0.33']
    functions=[lambda x:x,lambda x:x**2,lambda x:x**3,lambda x:x**4,lambda x:10**x,lambda x:10**-x,
       lambda x:x**-1, lambda x:np.log10(x),lambda x:np.log(x), lambda x:np.sqrt(x), lambda x:x**0.33]
    out=[]
    outNames=[]  
    for col in xVars.columns:
        for i in range(len(functions)):
            outNames.append(col+' '+functionNames[i])
            out.append(functions[i](xVars[col]))
    out=_list2arr(out)
    return out,outNames
   
#def standardize(xVars):
    
    
def importData():
	direc='R:\\Research\\GeologicalScience\\sdm\\DatasummaryMG\\'
	return pd.read_csv(direc+'train.csv'),pd.read_csv(direc+'test.csv')

 
def _list2arr(lis):
    arr=np.zeros((len(lis[0]),len(lis)))
    for i in range(len(lis)):
        arr[:,i]=np.array(lis[i])
    return arr