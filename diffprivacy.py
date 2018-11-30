#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:40:03 2018

@author: nkatebi
"""
import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np
def laplaceMechanism(x, epsilon):
    x +=  np.random.laplace(0, epsilon, 1)[0]
    return x

def Differential_Privacy(datapath,e):
    '''
    Input: path to the dataset and differential privacy parameter epsilon
    output: noisy histogram , error between noisy 
    histogram and original histogram for each epsilon 
    
    '''
    e=e.split(',')
    df=pd.read_csv(datapath)
    Age=df[df.columns[0]]
    NumberOfBins=int((max(Age)-min(Age))/5)
    counts, bins = np.histogram(Age,bins=NumberOfBins) #building histogram of data

   
    error=[];
    for epsilon in e:
        epsilon=float(epsilon)
        loc, scale = 0., max(Age)/epsilon
        sumvalue=0 
        newcount=[]
        
        for n in counts:
            new=int(n+np.random.laplace(loc, scale, 1)) # Adding laplace noise 
            if new<0:
                new=0
            newcount.append(new)
            sumvalue=sumvalue+np.abs(n-new)
        error.append(sumvalue/len(counts))
    
        plt.figure()
        plt.bar(bins[1:],counts,width=5,color="blue",edgecolor='red',linestyle = '-')
        plt.bar(bins[1:],newcount,width=5,color="blue",edgecolor='black',linestyle = '--')
        plt.xlabel('Age')
        plt.legend(['original histogram','noisy histogram'])
        plt.title('epsilon'+' = '+str(epsilon))
        plt.show()
    plt.figure()
    plt.plot(e,error) 
    plt.xlabel('epsilon')
    plt.ylabel('error')
    plt.show()
    
           
        
        
#datapath='adult_age_gender_race_dataset.csv'
#Differential_Privacy(datapath,[0.2,0.4,0.6,0.8,1])

if __name__== "__main__":
   Differential_Privacy(sys.argv[1],sys.argv[2])