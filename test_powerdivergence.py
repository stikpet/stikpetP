import pandas as pd
import numpy as np
from scipy.stats import chi2

def ts_powerdivergence(var1, var2=None, expCounts=None, lambd=2/3, corr=None):
    
    #Set correction factor to 1 (no correction)
    corFactor = 1
    
    #Test Used
    if lambd == 2/3 or lambd == "cressie-read":
        lambd = 2/3
        testUsed = "Cressie-Read"
    
    elif lambd==0 or lambd == "likelihood ratio":
        lambd=0
        testUsed = "likelihood-ratio"
        
    elif lambd==-1 or lambd == "mod-log":
        lambd=-1
        testUsed = "mod-log likelihood ratio"
        
    elif lambd==1 or lambd=="pearson":
        lambd=1
        testUsed = "Pearson chi-square"
    
    elif lambd==-0.5 or lambd=="freeman-tukey":
        lambd=-0.5
        testUsed = "Freeman-Tukey"
    elif lambd==-2 or lambd=="neyman":
        lambd==-2
        testUsed = "Neyman"
    else:
        testUsed = "power divergence with lambda = " + str(lambd)
        
        
    #The test itself
    
    if (var2 is None):
        #only one variable, so goodness-of-fit version
        
        freqs = var1.value_counts()
        k = len(freqs)
        
        #Determine expected counts if not provided
        if expCounts is None:
            expCounts = [sum(freqs)/len(freqs)]* k
            expCounts = pd.Series(expCounts, index=list(freqs.index.values))
        
        n = sum(freqs)
        df = k - 1
        
        #set williams correction factor
        if corr=="williams":
            corFactor = 1/(1 + (k**2 - 1)/(6*n*df))
            testUsed = testUsed + ", and Williams correction"
        
    else:
        #two variables, so use test of independence
        
        #create a cross table
        myCrosstable = pd.crosstab(var1, var2)
        colTotals = myCrosstable.sum()
        rowTotals = myCrosstable.sum(axis=1)
        n = sum(colTotals)
        r = len(rowTotals)
        c = len(colTotals)
        
        #Determine expected counts if not provided
        if expCounts is None:
            expCounts = myCrosstable.copy()
            for i in range(0, r):
                for j in range(0, c):
                    expCounts.iloc[i,j] = rowTotals[i]*colTotals[j]/n

            #convert the expected counts in the cross table to one long pandas series
            expCountsList = list(expCounts.iloc[:,0])
            for j in range(1,c):
                expCountsList = expCountsList + list(expCounts.iloc[:,j])
            expCounts = pd.Series(expCountsList) 
        
        #convert the frequencies in the cross table to one long pandas series
        freqsList = list(myCrosstable.iloc[:,0])
        for j in range(1,c):
            freqsList = freqsList + list(myCrosstable.iloc[:,j])
        freqs = pd.Series(freqsList) 
        
        df = (r - 1)*(c - 1)
        
        #set williams correction factor
        if corr=="williams":
            corFactor = 1/(1 + (n*sum(1/rowTotals) - 1)*(n*sum(1/colTotals) - 1)/(6*n*(r - 1)*(c - 1)))
            testUsed = testUsed + ", and Williams correction"
    
    #adjust frequencies if Yates correction is requested
    if corr=="yates":
        k = len(freqs)
        adjFreq = list(freqs).copy()
        for i in range(0, k):
            if adjFreq[i] > expCounts[i]:
                adjFreq[i] = adjFreq[i] - 0.5
            elif adjFreq[i] < expCounts[i]:
                adjFreq[i] = adjFreq[i] + 0.5

        freqs = pd.Series(adjFreq, index=list(freqs.index.values))
        testUsed = testUsed + ", and Yates correction"
    
    #determine the test statistic
    if lambd==0:
        ts = 2*sum(freqs*np.log(freqs/expCounts))
    elif lambd==-1:
        ts = 2*sum(expCounts*np.log(expCounts/freqs))
    else:
        ts = 2*sum(freqs*((freqs/expCounts)**(lambd) - 1))/(lambd*(lambd + 1))
    
    #set E.S. Pearson correction
    if corr=="pearson":
        corFactor = (n - 1)/n
        testUsed = testUsed + ", and Pearson correction"
    
    #Adjust test statistic
    ts = ts*corFactor
    
    #Determine p-value
    pVal = chi2.sf(ts, df)
    
    #Check minimum expected counts
    #Cells with expected count less than 5
    nbelow = len([x for x in expCounts if x < 5])
    #Number of cells
    ncells = len(expCounts)
    #As proportion
    pBelow = nbelow/ncells
    #the minimum expected count
    minExp = min(expCounts)
    
    #prepare results
    testResults = pd.DataFrame([[ts, df, pVal, minExp, pBelow*100, testUsed]], columns=["statistic", "df", "p-value", "minExp", "percBelow5", "test used"])        
    pd.set_option('display.max_colwidth', None)
    
    return testResults