import pandas as pd
import math
from scipy.stats import multinomial

def ts_trinomial_os(data, levels=None, mu = None):
    '''
    One-Sample Trinomial Test
    -------------------------
    
    A test that could be used with ordinal data that includes ties
    
    Parameters
    ----------
    data : list or pandas data series 
        the data
    levels : dictionary, optional
        the categories and numeric value to use
    mu : float, optional 
        hypothesized median. Default is the midrange of the data
        
    Returns
    -------
    testResults : pandas dataframe with 
    
    * "mu", the hypothesized median
    * "n-pos", the number scores above mu
    * "n-neg", the number scores below mu
    * "n-tied", the number of scores tied with mu
    * "p-value", significance (p-value)
    * "test", description of the test used
    
    Notes
    -----
    The test uses the trinomial probability mass function and can be found in Bian et al. (2009, p. 6).
    
    The formula used is:
    $$p = 2\\times \\sum_{i=n_d}^n \\sum_{j=0}^{\\lfloor \\frac{n - i}{2} \\rfloor} \\text{tri}\\left(\\left(j, j+i, n - i\\right), \\left(p_{pos}, p_{neg}, p_0\\right) \\right)$$
    
    With:
    $$p_0 = \\frac{n_0}{n}$$
    $$p_{pos} = p_{neg} = \\frac{1 - p_0}{n}$$
    $$\\left|n_{pos} - n_{neg}\\right|$$
    
    *Symbols used:*
    
    * \\(n_0\\), the number of scores equal to the hypothesized median
    * \\(n_{pos}\\), the number of scores above the hypothesized median
    * \\(n_{neg}\\), the number of scores below the hypothesized median
    * \\(p_0\\), the probability of the a score in the sample being equal to the hypothesized median
    * \\(p_{pos}\\), the population proportion of a score being above the hypothesized median
    * \\(p_{neg}\\), the population proportion of a score being below the hypothesized median
    * \\(\\text{tri}\\left(…,… \\right)\\), the trinomial probability mass function
    
    The paired version of the test is described in Bian et al. (1941), while Zaiontz (n.d.) mentions it can also be used for one-sample situations.
    
    References
    ----------
    Bian, G., McAleer, M., & Wong, W.-K. (2009). A trinomial test for paired data when there are many ties. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.1410589
    
    Zaiontz, C. (n.d.). Trinomial test. Real Statistics Using Excel. Retrieved March 2, 2023, from https://real-statistics.com/non-parametric-tests/trinomial-test/
    
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
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df2['Teach_Motivate']
    >>> order = {"Fully Disagree":1, "Disagree":2, "Neither disagree nor agree":3, "Agree":4, "Fully agree":5}
    >>> ts_trinomial_os(ex1, levels=order)
        mu  n-pos.  n-neg.  n-tied.   p-value                  test
    0  3.0      13      29       12  0.016261  one-sample trinomial

    Example 2: Numeric data
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> ts_trinomial_os(ex2)
        mu  n-pos.  n-neg.  n-tied.   p-value                  test
    0  3.0      10       6        2  0.385768  one-sample trinomial
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
    
    #remove missing values
    data = data.dropna()
    if levels is not None:
        data = data.replace(levels)
        data = pd.to_numeric(data)
    else:
        data = pd.to_numeric(data)
    
    #set hypothesized median to mid range if not provided
    if (mu is None):
        mu = (min(data) + max(data)) / 2
        
    nPos = sum(data>mu)
    nNeg = sum(data<mu)
    nNul = sum(data==mu)
    n = nPos + nNeg + nNul
    nd = abs(nPos-nNeg)

    pNul = nNul/n
    pPos = (1 - pNul)/2
    pNeg = pPos
    
    sig = 0
    for d in range(nd, n+1):
        for k in range(0, math.floor((n - d)/2)+1):
            pmf = multinomial.pmf([k, k + d, n-k-(k+d)], n, [pPos, pNeg, pNul])
            sig = sig + pmf
    
    sig = sig*2
    if sig>1:
        sig = 1
    
    testResults = pd.DataFrame([[mu, nPos, nNeg, nNul, sig, "one-sample trinomial"]], columns=["mu", "n-pos.", "n-neg.", "n-tied.", "p-value", "test"])
    pd.set_option('display.max_colwidth', None)
    
    return (testResults)