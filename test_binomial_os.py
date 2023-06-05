import pandas as pd
from scipy.stats import binom

def ts_binomial_os(data, codes=None, p0 = 0.5, twoSidedMethod="eqdist"):
    '''
    Single Binary Test - One-sample binomial
     
    This function will perform an exact one-sample binomial test, two-sided
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    codes : Optional list with the two codes to use
    p0 : Optional hypothesized proportion for the first category (default is 0.5)
    twoSidedMethod : Optional method to be used for 2-sided significance, either "eqdist" (default), "double", or "smallp"
        
    Returns
    -------
    testResults : Pandas dataframe with the two-sided significance (p-value) and test used
    
    Notes
    -------
    A one sided p-value is calculated first:
    $$sig_{one-tail} = B\\left(n, n_{min}, p_0^{\\ast}\\right)$$
    With:
    $$n_{min} = min\\left(n_s, n_f\\right)$$
    $$p_0^{\\ast} = \\begin{cases}p_0 & \\text{ if } n_{min}=n_s \\\ 1 - p_0 & \\text{ if } n_{min}= n_f\\end{cases}$$
    Where:
    \(n\) is the number of cases    
    \(n_s\) is the number of successes
    \(n_f\) is the number of failures
    \(p_0\) is the probability of a success according to the null hypothesis
    \(p_0^{\\ast}\) is the probability adjusted in case failures is used
    \(B\left(\dots\\right)\) the binomial cumulative distribution function
    
    For the two sided significance three options can be used.
    
    Option 1: Equal Distance Method (eqdist)
    $$sig_{two-tail} = B\\left(n, n_{min}, p_0^{\\ast}\\right) + 1 - B\\left(n, \\left \\lfloor 2 \\times n_0 \\right \\rfloor - n_{min} - 1, p_0^{\\ast}\\right)$$
    With:
    \(n_0 = \\left\\lfloor n\\times p_0\\right\\rfloor\)
    
    This method looks at the number of cases. In a sample of \(n\) people, we’d then expect \(n_0 = \\left\\lfloor n\\times p_0\\right\\rfloor\) successes (we round the result down to the nearest integer). We only had \(n_{min}\), so a difference of \(n_0-n_{min}\). The ‘equal distance method’ now means to look for the chance of having \(k\) or less, and \(n_0+n_0-n_{min}=2\\times n_0-n_{min}\) or more. Each of these two probabilities can be found using a binomial distribution. Adding these two together than gives the two-sided significance. 
    
    Option 2: Small p-method
    $$sig_{two-tail} = B\\left(n, n_{min}, p_0^{\\ast}\\right) + \\sum_{i=n_{min}+1}^n \\begin{cases} 0 & \\text{ if } b\\left(n, i, p_0^{\\ast}\\right)> b\\left(n, n_{min}, p_0^{\\ast}\\right) \\\ b\\left(n, i, p_0^{\\ast}\\right)& \\text{ if } \\times \\leq  b\\left(n, i, p_0^{\\ast}\\right)> b\\left(n, n_{min}, p_0^{\\ast}\\right) \\end{cases}$$
    With:
    \(b\\times\\left(\\dots\\right)\) as the binomial probability mass function.
    
    This method looks at the probabilities itself. \(b\\left(n, n_{min}, p_0^{\\ast}\\right)\) is the probability of having exactly \(n_{min}\) out of a group of n, with a chance \(p_0^{\\ast}\) each time. The method of small p-values now considers ‘or more extreme’ any number between 0 and n (the sample size) that has a probability less or equal to this. This means we need to go over each option, determine the probability and check if it is lower or equal. So, the probability of 0 successes, the probability of 1 success, etc. The sum for all of those will be the two-sided significance. We can reduce the work a little since any value below \(n_{min}\), will also have a lower probability, so we only need to sum over the ones above it and add the one-sided significance to the sum of those.
    
    Option 3: Double single
    $$sig_{two-tail} = 2\\times sig_{one-tail}$$
    
    Fairly straight forward. Just double the one-sided significance.
   
    Notes
    -----
    It uses scipy.stats' binom_test
    
    Examples
    ------
    >>> dataList = ['Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female']
    >>> data = pd.Series(dataList)
    >>> codes = ['Female', 'Male']
    >>> ts_binomial_os(data, codes)
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    
    testUsed = "one-sample binomial"
    
    #Determine number of successes, failures, and total sample size
    if codes is None:
        freq = data.value_counts()
        n = sum(freq.values)
        n1 = freq.values[0]
        n2 = n - n1
    
    else:        
        n1 = sum(data==codes[0])
        n2 = sum(data==codes[1])
        n = n1 + n2
    
    minCount = n1
    ExpProp = p0
    if n2 < n1:
        minCount = n2
        ExpProp = 1 - p0
        
    #one sided test
    sig1 = binom.cdf(minCount,n,ExpProp)  
    
    #two sided
    if twoSidedMethod=="double":
        sigR = sig1
        testUsed = testUsed + ", with double one-sided method"
    
    elif twoSidedMethod=="eqdist":
        #Equal distance
        ExpCount = n * ExpProp
        Dist = ExpCount - minCount
        RightCount = ExpCount + Dist
        sigR = 1 - binom.cdf(RightCount - 1,n,ExpProp)
        testUsed = testUsed + ", with equal-distance method"
        
    else:
        #Method of small p
        binSmall = binom.pmf(minCount, n, ExpProp)
        sigR = 0
        for i in range((minCount + 1),n+1):
            binDist = binom.pmf(i, n, ExpProp)
            if (binDist <= binSmall):
                sigR = sigR + binDist
        testUsed = testUsed + ", with small p method"
        
    sig2 = sig1 + sigR
    
    testResults = pd.DataFrame([[sig2, testUsed]], columns=["p-value (2-sided)", "test"])
    
    return testResults