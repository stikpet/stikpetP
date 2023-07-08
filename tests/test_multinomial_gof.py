import itertools as it
import pandas as pd
import numpy as np
from scipy.stats import multinomial

def ts_multinomial_gof(data, expCounts=None):
    '''
    Multinomial Goodness-of-Fit Test
    --------------------------------
     
    A test that can be used with a single nominal variable, to test if the probabilities in all the categories are equal (the null hypothesis). If the test has a p-value below a pre-defined threshold (usually 0.05) the assumption they are all equal in the population will be rejected. 
    
    There are quite a few tests that can do this. Perhaps the most commonly used is a Pearson chi-square test, but also a G-test, Freeman-Tukey, Neyman, Mod-Log Likelihood and Cressie-Read test are possible.
    
    McDonald (2014, p. 82) suggests to always use this exact test as long as the sample size is less than 1000 (which was just picked as a nice round number, when n is very large the exact test becomes computational heavy even for computers).
    
    Parameters
    ----------
    data : list or pandas data series
    expCounts : pandas data frame, optional 
        the categories and expected counts
        
    Returns
    -------
    testResults : Pandas dataframe with the probability of the observed frequencies, number of combinations used, significance (p-value) and test used
   
    Notes
    -----
    It uses the itertools, pandas, numpy and scipy's stats multinomial function
    
    The exact multinomial test of goodness of fit is done in four steps
    
    Step 1: Determine the probability of the observed counts using the probability mass function of the multinomial distribution
    
    Step 2: Determine all possible permutations with repetition that create a sum equal to the sample size over the k-categories.
    
    Step 3: Determine the probability of each of these permutations using the probability mass function of the multinomial distribution.
    
    Step 4: Sum all probabilities found in step 3 that are equal or less than the one found in step 1.
    
    References 
    ----------
    McDonald, J. H. (2014). *Handbook of biological statistics* (3rd ed.). Sparky House Publishing.

    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    ---------
    >>> pd.set_option('display.width',1000)
    >>> pd.set_option('display.max_columns', 1000)
    
    Example 1: pandas series
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['mar1'][0:20]
    >>> ts_multinomial_gof(ex1)
        p obs.  n combs.   p-value                                               test
    0  0.00022      8855  0.199807  one-sample multinomial exact goodness-of-fit test
    
    Example 2: pandas series with various settings
    >>> ex2 = df1['mar1'][0:20]
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,5]})
    >>> ts_multinomial_gof(ex2, expCounts=eCounts)
         p obs.  n combs.   p-value                                               test
    0  0.003209      1330  0.390236  one-sample multinomial exact goodness-of-fit test
    
    Example 3: a list
    >>> ex3 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> ts_multinomial_gof(ex3)
         p obs.  n combs.   p-value                                               test
    0  0.002541      1540  0.388712  one-sample multinomial exact goodness-of-fit test

    '''
    
    if type(data) == list:
        data = pd.Series(data)
        
    #determine the observed counts
    
    if expCounts is None:
        #generate frequency table
        freq = data.value_counts()
        n = sum(freq)
        freq = freq.rename_axis('category').reset_index(name='count')
        
        #number of categories to use (k)
        k = len(freq)
        
        #number of expected counts is simply sample size
        nE = n
    else:
        #if expected counts are given
        
        #number of categories to use (k)
        k = len(expCounts)
        
        freq = pd.DataFrame(columns = ["category", "count"])
        for i in range(0, k):
            nk = data[data==expCounts.iloc[i, 0]].count()
            lk = expCounts.iloc[i, 0]
            freq = pd.concat([freq, pd.DataFrame([{"category": lk, "count": nk}])])
        nE = sum(expCounts.iloc[:,1])
            
        freq = freq.reset_index(drop=True)
            
    n = sum(freq["count"])
    
    #the true expected counts
    if expCounts is None:
        #assume all to be equal
        exp_prop = [1/k] * k
        
    else:
        #check if categories match
        exp_prop = []
        for i in range(0,k):
            exp_prop.append(expCounts.iloc[i, 1]/nE)
    
    observed = freq.iloc[:,1]
    p_obs = multinomial.pmf(x=np.sort(observed), n=n, p=exp_prop)
    counts = np.arange(0, n + 1)

    all_perm = np.asarray(list(it.product(counts, repeat=k)))
    sum_perm = all_perm[np.sum(all_perm, axis=1) == n]
    ncomb = len(sum_perm)

    p_val = 0
    for i in sum_perm:
        p_perm = multinomial.pmf(x=i, n=n, p=exp_prop)
        if p_perm <= p_obs:
            p_val = p_val + p_perm        

            
    testUsed = "one-sample multinomial exact goodness-of-fit test"
    testResults = pd.DataFrame([[p_obs, ncomb, p_val, testUsed]], columns=["p obs.", "n combs.", "p-value", "test"])
    pd.set_option('display.max_colwidth', None)
    
    return testResults