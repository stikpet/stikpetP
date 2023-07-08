import pandas as pd
import numpy as np
from scipy.stats import chi2

def ts_neyman_gof(data, expCounts=None, cc=None):
    '''
    Neyman Test of Goodness-of-Fit
    ------------------------------
    
    A test that can be used with a single nominal variable, to test if the probabilities in all the categories are equal (the null hypothesis). If the test has a p-value below a pre-defined threshold (usually 0.05) the assumption they are all equal in the population will be rejected.
    
    There are quite a few tests that can do this. Perhaps the most commonly used is the Pearson chi-square test, but also an exact multinomial, G-test, Freeman-Tukey, Mod-Log Likelihood, Cressie-Read, and Freeman-Tukey-Read test are possible.
    
    Parameters
    ----------
    data :  list or pandas data series 
        the data
    expCount : pandas dataframe, optional 
        the categories and expected counts
    cc : {None, "yates", "pearson", "williams"}, optional 
        which continuity correction to use. Default is None
    
    Returns
    -------
    testResults : pandas dataframe with 
    
    * *n*, the sample size
    * *k*, the number of categories
    * *statistic*, the test statistic (chi-square value)
    * *df*, degrees of freedom
    * *p-value*, significance (p-value)
    * *minExp*, the minimum expected count
    * *propBelow5*, the proportion of categories with an expected count below 5
    * *test*, description of the test used
    
    Notes
    -----
    The formula used is (Neyman, 1949, p. 250):
    $$\\chi_{N}^{2}=\\sum_{i=1}^{k}\\frac{\\left(O_{i}-E_{i}\\right)^{2}}{O_{i}}$$
    $$df = k - 1$$
    $$sig. = 1 - \\chi^2\\left(T^{2},df\\right)$$
    
    With:
    $$n = \\sum_{i=1}^k F_i$$
    
    If no expected counts provided:
    $$E_i = \\frac{n}{k}$$
    else:
    $$E_i = n\\times\\frac{E_{p_i}}{n_p}$$
    $$n_p = \\sum_{i=1}^k E_{p_i}$$
    
    *Symbols used:*
    
    * \\(k\\) the number of categories
    * \\(F_i\\) the (absolute) frequency of category i
    * \\(E_i\\) the expected frequency of category i
    * \\(E_{p_i}\\) the provided expected frequency of category i
    * \\(n\\) the sample size, i.e. the sum of all frequencies
    * \\(n_p\\) the sum of all provided expected counts
    * \\(\\chi^2\\left(\\dots\\right)\\) the chi-square cumulative density function
        
    The Yates continuity correction (cc="yates") is calculated using (Yates, 1934, p. 222):
    $$F_i^\\ast  = \\begin{cases} F_i - 0.5 & \\text{ if } F_i > E_i \\\\ F_i + 0.5 & \\text{ if } F_i < E_i \\\\ F_i & \\text{ if } F_i = E_i \\end{cases}$$
    $$MG_Y=2\\times\\sum_{i=1}^{k}\\left(F_i^\\ast\\times ln\\left(\\frac{F_i^\\ast}{E_{i}}\\right)\\right)$$
    Where if \\(F_i^\\ast = 0\\) then \\(F_i^\\ast\\times ln\\left(\\frac{F_i^\\ast}{E_{i}}\\right) = 0\\).
    
    The Pearson correction (cc="pearson") is calculated using (E.S. Pearson, 1947, p. 157):
    $$\\chi_{PP}^2 = \\chi_{P}^{2}\\times\\frac{n - 1}{n}$$
    
    The Williams correction (cc="williams") is calculated using (Williams, 1976, p. 36):
    $$\\chi_{PW}^2 = \\frac{\\chi_{P}^2}{q}$$
    
    With:
    $$q = 1 + \\frac{k^2 - 1}{6\\times n\\times df}$$
    
    The formula is also used by McDonald (2014, p. 87)
    
    References
    ----------
    Neyman, J. (1949). Contribution to the theory of the chi-square test. *Berkeley Symposium on Math. Stat, and Prob*, 239–273. https://doi.org/10.1525/9780520327016-030
    
    Pearson, E. S. (1947). The choice of statistical tests illustrated on the Interpretation of data classed in a 2 × 2 table. *Biometrika, 34*(1/2), 139–167. https://doi.org/10.2307/2332518
    
    Williams, D. A. (1976). Improved likelihood ratio tests for complete contingency tables. *Biometrika, 63*(1), 33–37. https://doi.org/10.2307/2335081
    
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
    
    Example 1: pandas series
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['mar1']
    >>> ts_neyman_gof(ex1)
          n  k    statistic  df  p-value  minExp  percBelow5 test used
    0  1941  5  1815.669122   4      0.0   388.2         0.0    Neyman
    
    Example 2: pandas series with various settings
    >>> ex2 = df1['mar1']
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,5]})
    >>> ts_neyman_gof(ex2, expCounts=eCounts, cc="yates")
          n  k   statistic  df  p-value  minExp  percBelow5                     test used
    0  1760  4  1980.58683   3      0.0     440         0.0  Neyman, and Yates correction
    >>> ts_neyman_gof(ex2, expCounts=eCounts, cc="pearson")
          n  k    statistic  df  p-value  minExp  percBelow5                       test used
    0  1760  4  1995.362585   3      0.0     440         0.0  Neyman, and Pearson correction
    >>> ts_neyman_gof(ex2, expCounts=eCounts, cc="williams")
          n  k    statistic  df  p-value  minExp  percBelow5                        test used
    0  1760  4  1995.552094   3      0.0     440         0.0  Neyman, and Williams correction
    
    Example 3: a list
    >>> ex3 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> ts_neyman_gof(ex3)
        n  k  statistic  df   p-value  minExp  percBelow5 test used
    0  19  4   4.905506   3  0.178849    4.75       100.0    Neyman
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
        
    #Set correction factor to 1 (no correction)
    corFactor = 1    
    testUsed = "Neyman"
    
    #The test itself        
    freqs = data.value_counts()
    k = len(freqs)

    #Determine expected counts if not provided
    if expCounts is None:
        expCounts = [sum(freqs)/len(freqs)]* k
        expCounts = pd.Series(expCounts, index=list(freqs.index.values))
    
    else:
        #if expected counts are provided
        ne = 0
        k = len(expCounts)
        #determine sample size of expected counts
        for i in range(0,k):
            ne = ne + expCounts.iloc[i,1]

        #remove categories not provided from observed counts
        for i in freqs.index:
            if i not in list(expCounts.iloc[:,0]):
                freqs = freqs.drop(i)

        #adjust based on observed count total
        n = sum(freqs)
        for i in range(0,k):
            expCounts.iloc[i,1] = expCounts.iloc[i,1]/ne * n
        
        expCounts = pd.Series(expCounts.iloc[:, 1])

    n = sum(freqs)
    df = k - 1

    #set williams correction factor
    if cc=="williams":
        corFactor = 1/(1 + (k**2 - 1)/(6*n*df))
        testUsed = testUsed + ", and Williams correction"
    
    #adjust frequencies if Yates correction is requested
    if cc=="yates":
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
    ts = sum((list(freqs) - expCounts)**2/list(freqs))
    
    #set E.S. Pearson correction
    if cc=="pearson":
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
    testResults = pd.DataFrame([[n, k, ts, df, pVal, minExp, pBelow*100, testUsed]], columns=["n", "k","statistic", "df", "p-value", "minExp", "percBelow5", "test used"])        
    pd.set_option('display.max_colwidth', None)
    
    return testResults