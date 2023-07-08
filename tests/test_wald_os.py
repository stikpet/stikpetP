import pandas as pd
from statistics import NormalDist

def ts_wald_os(data, codes=None, p0 = 0.5, cc = None):
    '''
    One-sample Wald Test
    --------------------
     
    A one-sample score test could be used with binary data, to test if the two categories have a significantly different proportion. It is an approximation of a binomial test, by using a standard normal distribution. Since the binomial distribution is discrete while the normal is continuous, a so-called continuity correction can (should?) be applied.
    
    The null hypothesis is usually that the proportions of the two categories in the population are equal (i.e. 0.5 for each). If the p-value of the test is below the pre-defined alpha level (usually 5% = 0.05) the null hypothesis is rejected and the two categories differ in proportion significantly.
    
    The input for the function doesn't have to be a binary variable. A nominal variable can also be used and the two categories to compare indicated.
    
    A significance in general is the probability of a result as in the sample, or more extreme, if the null hypothesis is true. 
    
    Some info on the different tests can be found at https://youtu.be/jQ-nSPTGOgE.
    
    Parameters
    ----------
    data : list or pandas data series 
        the data
    codes : list, optional 
        the two codes to use. Default will use the first two found
    p0 : float, optional
        the hypothesized proportion for the first category. Default is 0.5
    cc : {None, "yates"}, optional
        continuity correction to use. Default is None
        
    Returns
    -------
    testResults : pandas dataframe with 
    
    * *n*, the sample size
    * *statistic*, test statistic (z-value)
    * *p-value (2-sided)*, two-sided significance (p-value)
    * *test*, test used
   
    Notes
    -----
    This test differs from the one-sample score test in the calculation of the standard error. For the ‘regular’ version this is based on the expected proportion, while for the Wald version it is done with the observed proportion.
    
    The formula used (Wald, 1943):
    $$z=\\frac{x - \\mu}{SE}$$
    
    With:
    $$\\mu = n\\times p_0$$
    $$SE = \\sqrt{x\\times\\left(1 - \\frac{x}{n}\\right)}$$
    
    *Symbols used:*
    
    * \\(x\\) is the number of successes in the sample
    * \\(p_0\\) the expected proportion (i.e. the proportion according to the null hypothesis)
    
    If the Yates continuity correction is used the formula changes to (Yates, 1934, p. 222):
    $$z_{Yates} = \\frac{\\left|x - \\mu\\right| - 0.5}{SE}$$
    
    The formula used in the calculation is the one from IBM (2021, p. 997). IBM refers to Agresti, most likely Agresti (2013, p. 10), who in turn refer to Wald (1943)
    
    References
    ----------
    Agresti, A. (2013). *Categorical data analysis* (3rd ed.). Wiley.
    
    IBM SPSS Statistics Algorithms. (2021). IBM.
    
    Wald, A. (1943). Tests of statistical hypotheses concerning several parameters when the number of observations is large. *Transactions of the American Mathematical Society, 54*(3), 426–482. https://doi.org/10.2307/1990256
    
    Yates, F. (1934). Contingency tables involving small numbers and the chi square test. *Supplement to the Journal of the Royal Statistical Society, 1*(2), 217–235. https://doi.org/10.2307/2983604

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
    
    Example 1: Numeric list
    >>> ex1 = [1, 1, 2, 1, 2, 1, 2, 1]
    >>> ts_wald_os(ex1)
       n  statistic  p-value (2-sided)                test
    0  8  -0.730297           0.465209  Wald approximation
    >>> ts_wald_os(ex1, p0=0.3)
       n  statistic  p-value (2-sided)                test
    0  8  -1.898772           0.057595  Wald approximation
    >>> ts_wald_os(ex1, p0=0.3, cc="yates")
       n  statistic  p-value (2-sided)                                                 test
    0  8  -1.496663           0.134481  Wald approximation with Yates continuity correction
    
    Example 2: pandas Series
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ts_wald_os(df1['sex'])
          n  statistic  p-value (2-sided)                test
    0  1974  -4.570499           0.000005  Wald approximation
    >>> ts_wald_os(df1['mar1'], codes=["DIVORCED", "NEVER MARRIED"])
         n  statistic  p-value (2-sided)                test
    0  709  -3.062068           0.002198  Wald approximation
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
        
    nrows = len(data)
    
    if codes is None:
        k1 = data[0]
        i = 1
        while pd.isna(k1) and i < nrows:
            k1 = data[i]
            i = i + 1
    
        k2 = data[i]
        i = i + 1
        while (pd.isna(k2) or k2==k1) and i < nrows:
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
        
    #Wald approximation
    if cc is None:
        p = minCount / n
        q = 1 - p
        se = (p * (1 - p) / n)**0.5
        Z = (p - ExpProp) / se
        sig2 = 2 * (1 - NormalDist().cdf(abs(Z)))
        testValue = Z
        testUsed = "Wald approximation"
    elif (cc == "yates"):
        #Wald approximation with continuity correction
        p = (minCount + 0.5) / n
        q = 1 - p
        se = (p * (1 - p) / n)**0.5
        Z = (p - ExpProp) / se
        sig2 = 2 * (1 - NormalDist().cdf(abs(Z)))
        testValue = Z
        testUsed = "Wald approximation with Yates continuity correction"
        
    testResults = pd.DataFrame([[n, testValue, sig2, testUsed]], columns=["n", "statistic", "p-value (2-sided)", "test"])
    
    return (testResults)

#example
dataList = ['Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female']
data = pd.Series(dataList)
codes = ['Female', 'Male']

ts_wald_os(data, codes)