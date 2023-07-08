import pandas as pd
from ..tests.test_binomial_os import ts_binomial_os

def ph_binomial(data, expCount=None, twoSidedMethod='eqdist', posthoc = "bonferroni"):
    '''
    Pairwise Binomial Test for Post-Hoc Analysis
    --------------------------------------------
    
    This function will perform a one-sample binomial test for each possible pair in the data. It makes use of the ts_binomial_os() function.
    
    Parameters
    ----------
    data : list or pandas series
    expCount : pandas dataframe, optional 
        categories and expected counts
    twoSidedMethod : string, optional
        method to use for determining two-sided p-value of binomial test. See ts_binomial_os()
    posthoc : string, optional
        the correction to use, currently only "bonferroni" available
    
    Returns
    -------
    res : pandas dataframe with:
    
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
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    >>> pd.set_option('display.width',1000)
    >>> pd.set_option('display.max_columns', 1000)
    
    Example 1: pandas series    
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['mar1']
    >>> ph_binomial(ex1)
          category 1     category 2   n1   n2  obs. prop. cat. 1  exp. prop. cat. 1        p-value   adj. p-value
    0        MARRIED  NEVER MARRIED  972  395           0.711046                0.5   1.052263e-56   1.052263e-55
    1        MARRIED       DIVORCED  972  314           0.755832                0.5   7.829174e-79   7.829174e-78
    2        MARRIED        WIDOWED  972  181           0.843018                0.5  1.407217e-131  1.407217e-130
    3        MARRIED      SEPARATED  972   79           0.924833                0.5  1.267980e-196  1.267980e-195
    4  NEVER MARRIED       DIVORCED  395  314           0.557123                0.5   2.635704e-03   2.635704e-02
    5  NEVER MARRIED        WIDOWED  395  181           0.685764                0.5   1.352112e-19   1.352112e-18
    6  NEVER MARRIED      SEPARATED  395   79           0.833333                0.5   7.075688e-52   7.075688e-51
    7       DIVORCED        WIDOWED  314  181           0.634343                0.5   2.401379e-09   2.401379e-08
    8       DIVORCED      SEPARATED  314   79           0.798982                0.5   1.472395e-34   1.472395e-33
    9        WIDOWED      SEPARATED  181   79           0.696154                0.5   2.223544e-10   2.223544e-09
    
    Example 2: pandas series with various settings
    >>> ex2 = df1['mar1']
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,5]})
    >>> ph_binomial(ex2, expCount=eCounts)
          category 1     category 2   n1   n2  obs. prop. cat. 1  exp. prop. cat. 1        p-value   adj. p-value
    0        MARRIED       DIVORCED  972  314           0.755832                0.5   7.829174e-79   4.697504e-78
    1        MARRIED  NEVER MARRIED  972  395           0.711046                0.5   1.052263e-56   6.313581e-56
    2        MARRIED      SEPARATED  972   79           0.924833                0.5  1.267980e-196  7.607878e-196
    3       DIVORCED  NEVER MARRIED  314  395           0.442877                0.5   2.635704e-03   1.581423e-02
    4       DIVORCED      SEPARATED  314   79           0.798982                0.5   1.472395e-34   8.834367e-34
    5  NEVER MARRIED      SEPARATED  395   79           0.833333                0.5   7.075688e-52   4.245413e-51

    Example 3: a list
    >>> ex3 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> ph_binomial(ex3)
          category 1     category 2  n1  n2  obs. prop. cat. 1  exp. prop. cat. 1   p-value  adj. p-value
    0       DIVORCED        MARRIED   7   6           0.538462                0.5  1.000000             1
    1       DIVORCED  NEVER MARRIED   7   4           0.636364                0.5  0.548828             1
    2       DIVORCED      SEPARATED   7   2           0.777778                0.5  0.179688             1
    3        MARRIED  NEVER MARRIED   6   4           0.600000                0.5  0.753906             1
    4        MARRIED      SEPARATED   6   2           0.750000                0.5  0.289062             1
    5  NEVER MARRIED      SEPARATED   4   2           0.666667                0.5  0.687500             1

    '''
    if type(data) is list:
        data = pd.Series(data)
        
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