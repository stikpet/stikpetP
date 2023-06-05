import pandas as pd
from statistics import NormalDist

def ts_score_os(data, codes = None, p0 = 0.5, cc = None):
    '''
    Single Binary Test - One-sample Score
     
    A one-sample score test could be used with binary data, to test if the two categories have a significantly different proportion. It is an approximation of a binomial test, by using a standard normal distribution. Since the binomial distribution is discrete while the normal is continuous, a so-called continuity correction can (should?) be applied.
    
    The null hypothesis is usually that the proportions of the two categories in the population are equal (i.e. 0.5 for each). If the p-value of the test is below the pre-defined alpha level (usually 5% = 0.05) the null hypothesis is rejected and the two categories differ in proportion significantly.
    
    The input for the function doesn't have to be a binary variable. A nominal variable can also be used and the two categories to compare indicated. A significance in general is the probability of a result as in the sample, or more extreme, if the null hypothesis is true. 
    
    Some info on the different tests can be found in https://youtu.be/jQ-nSPTGOgE.
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    codes : optional list with the two codes to use, default is first two found
    p0 : The hypothesized proportion for the first category (default is 0.5)
    cc : use continuity correction, either None (default), or "yates"
        
    Returns
    -------
    testResults : Pandas dataframe with the test statistic, two-sided significance (p-value) and test used
   
    Notes
    -----
    
    Also sometimes called a 'proportion' test.
    The formula used is (Wilson, 1927):
    $$z=\\frac{x - \\mu}{SE}$$
    
    With:
    $$\\mu = n\\times p_0$$
    $$SE=\\sqrt{\\mu\\times\\left(1-p_0\\right)}$$
    
    Symbols used:
    
    * \(x\) is the number of successes in the sample
    * \(p_0\) the expected proportion (i.e. the proportion according to the null hypothesis)
        
    If the Yates continuity correction is used the formula changes to (Yates, 1934, p. 222):
    $$z_{Yates} = \\frac{\\left|x - \\mu\\right| - 0.5}{SE}$$
    
    The formula used and naming comes from IBM (2021, p. 997) who refer to Agresti, most likeli Agresti (2013, p. 10)

    It uses NormalDist from Python's statistics library
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    References
    ----------
    Agresti, A. (2013). *Categorical data analysis* (3rd ed.). Wiley.
    
    IBM SPSS Statistics Algorithms. (2021). IBM.
    
    Wilson, E. B. (1927). Probable Inference, the Law of Succession, and Statistical Inference. *Journal of the American Statistical Association, 22*(158), 209–212. https://doi.org/10.2307/2276774
    
    Yates, F. (1934). Contingency tables involving small numbers and the chi square test. *Supplement to the Journal of the Royal Statistical Society, 1*(2), 217–235. https://doi.org/10.2307/2983604
    
    Examples
    --------
    >>> dataList = ["Female", "Male", "Male", "Female", "Male", "Male"]
    >>> data = pd.Series(dataList)
    >>> codes = ['Female', 'Male']
    >>> ts_score_os(data, codes)
    
    '''
    
    if (codes is None):
        k1 = data[0]
        i = 1
        if (pd.isna(k1)):            
            while (pd.isna(k1)):
                k1 = data[i]
                i = i + 1
        
        k2 = data[i]
        if (pd.isna(k2) or k2==k1):            
            while (pd.isna(k2) or k2==k1):
                k2 = data[i]
                i = i + 1
    else:
        k1 = codes[0]
        k2 = codes[1]
        
    #Determine number of successes
    n1 = sum(data==k1)
    n2 = sum(data==k2)
    n = n1 + n2
    
    minCount = n1
    ExpProp = p0
    if (n2 < n1):
        minCount = n2
        ExpProp = 1 - ExpProp
        
    #Normal approximation
    if (cc is None):
        p = minCount / n
        q = 1 - p
        se = (p0 * (1 - p0) / n)**0.5
        Z = (p - ExpProp) / se
        sig2 = 2 * (1 - NormalDist().cdf(abs(Z)))
        testValue = Z
        testUsed = "Normal approximation"
    elif not (cc is None) and (cc == "yates"):
        #Normal approximation with continuity correction
        p = (minCount + 0.5) / n
        q = 1 - p
        se = (p0 * (1 - p0) / n)**0.5
        Z = (p - ExpProp) / se
        sig2 = 2 * (1 - NormalDist().cdf(abs(Z)))
        testValue = Z
        testUsed = "Normal approximation with Yates continuity correction"
        
    testResults = pd.DataFrame([[testValue, sig2, testUsed]], columns=["statistic", "p-value (2-sided)", "test"])
    
    return (testResults)