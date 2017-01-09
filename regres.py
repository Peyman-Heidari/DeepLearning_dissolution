# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:18:04 2016

@author: mggm6
"""

from sklearn import linear_model
import matplotlib.pyplot as plt
import usefulFuncs as uf
import pandas as pd
import sklearn.preprocessing as preprocessing
import numpy as np

direc='R:\\Research\\GeologicalScience\\sdm\\DatasummaryMG\\'
	
train = pd.read_csv(direc+'train.csv')
test = pd.read_csv(direc+'test.csv')

train,test=uf.importData()


 
X_train=train[['MajorAnisotropy','MinAnisotropy','pH','MagnesitePercentageInitial','MgPerm','kratio']]#select out variables that we are interested in\n",
y_train=train['poriosity_change']
   
X_test=test[['MajorAnisotropy','MinAnisotropy','pH','MagnesitePercentageInitial','MgPerm', 'kratio']]#select out variables that we are interested in\n",
y_test=test['poriosity_change']


X_train,X_trainNames=uf.xTransform(X_train)
X_test,X_testNames=uf.xTransform(X_test)

print('start')
for i in range(X_test.shape[0]):
    for j in range(X_test.shape[1]):
        if X_test[i,j]>1.7e308 or X_test[i,j]<-1.7e308 or np.isnan(X_test[i,j]) or np.isinf(X_test[i,j]):
            print(i,j)



preproc = preprocessing.StandardScaler()
preproc = preproc.fit(X_train)
X_train = preproc.transform(X_train)
X_test = preproc.transform(X_test)
#LASSO
model = linear_model.LassoCV(fit_intercept=False,max_iter=100000)
model = model.fit(X_train, y_train)
score = model.score(X_test, y_test)
lassocv_alpha = model.alpha_
print(score)
display=[i for i in zip(X_trainNames,model.coef_) if i[1]!=0.0]
print(display) 

Lresults=[i for i in range(len(model.coef_)) if model.coef_[i]!=0.0]
newxtrain= X_train[:,Lresults]
newxtest= X_test[:,Lresults]

#Linear using selected parameters
Model= linear_model.LinearRegression()
Model= Model.fit(newxtrain,y_train)
ScoreL= Model.score(newxtest,y_test)
print(ScoreL)
displayLinear=[i for i in zip(display,Model.coef_)]
print(displayLinear)

