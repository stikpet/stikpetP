import pandas as pd
from .test_binomial_os import ts_binomial_os

def ph_binomial(data, expCount=None, twoSidedMethod='eqdist', posthoc = "bonferroni"):
    '''
    Pairwise Binomial Test for Post-Hoc Analysis
    
    This function will perform a one-sample binomial test for each possible pair in the data. It makes use of the ts_binomial_os() function.
    
    Parameters
    ----------
    data : Pandas series with the data
    expCount : optional pandas dataframe with categories and expected counts
    twoSidedMethod : method to use for determining two-sided p-value of binomial test
    posthoc : the correction to use, currently only "bonferroni" available
    
    Returns
    -------
    Pandas dataframe with:
    * *category 1*, the label of the first category
    * *category 2*, the label of the second category
    * *n1*, the sample size of the first category
    * *n2*, the sample size of the second category 
    * *obs. prop. cat. 1*, the proportion in the sample of the first category
    * *exp. prop. cat. 1*, the expected proportion for the first category
    * *p-value*, the unadjusted significance
    * *adj. p-value*, the adjusted significance
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> ph_binomial(data, eCounts)
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,15]})
    >>> ph_binomial(data, eCounts)
    
    '''
    
    freq = data.value_counts()
    
    if expCount is None:
        #assume all to be equal
        n = sum(freq)
        k = len(freq)
        categories = list(freq.index)
        expC = [n/k] * k
        
    else:
        #check if categories match
        nE = 0
        n = 0
        for i in range(0, len(expCount)):
            nE = nE + expCount.iloc[i,1]
            n = n + freq[expCount.iloc[i,0]]
        
        expC = []
        for i in range(0,len(expCount)):
            expC.append(expCount.iloc[i, 1]/nE*n)
            
        k = len(expC)
        categories = list(expCount.iloc[:,0])
    

    res = pd.DataFrame(columns=["category 1", "category 2", "n1", "n2", "obs. prop. cat. 1", "exp. prop. cat. 1", "p-value", "adj. p-value"])

    adjFactor = k * (k - 1)/ 2
    for i in range(0, k-1):
        for j in range(i+1, k):
            n1 = freq[categories[i]]
            n2 = freq[categories[j]]
            obP1 = n1/(n1 + n2)
            exP1 = expC[i]/(expC[i]+expC[j])

            codes = [categories[i], categories[j]]
            sig = ts_binomial_os(data, codes=codes, p0 = exP1)["p-value (2-sided)"][0]
            
            if posthoc == "bonferroni":
                adjSig = sig*adjFactor
            if adjSig > 1:
                adjSig = 1
            res.loc[len(res)] = [categories[i], categories[j], n1, n2, obP1, exP1, sig, adjSig]

    return res