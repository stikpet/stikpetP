import pandas as pd
from scipy.stats import binom

def ts_sign_os(data, levels=None, mu = None):
    '''
    One-Sample Sign Test
    --------------------
     
    This function will perform one-sample sign test.
    
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
    
    * *p-value*, the significance (p-value) 
    * *test*, description of the test used
   
    Notes
    -----
    this uses the binom function from scipy.stats for the binomial distribution cdf.
    
    The test statistic is calculated using (Stewart, 1941, p. 236):
    $$p = 2\\times B\\left(n, \\text{min}\\left(n_+, n_-\\right), \\frac{1}{2}\\right)$$
    
    *Symbols used:*
    
    * \\(B\\left(\\dots\\right)\\) is the binomial cumulative distribution function
    * \\(n\\) is the number of cases
    * \\(n_+\\) is the number of cases above the hypothesized median
    * \\(n_-\\) is the number of cases below the hypothesized median
    * \\(min\\) is the minimum value of the two values
    
    The test is described in Stewart (1941), although there are earlier uses. The paired version for example was already described by Arbuthnott (1710)
    
    References
    ----------
    Arbuthnott, J. (1710). An argument for divine providence, taken from the constant regularity observ’d in the births of both sexes. *Philosophical Transactions of the Royal Society of London, 27*(328), 186–190. https://doi.org/10.1098/rstl.1710.0011
    
    Stewart, W. M. (1941). A note on the power of the sign test. *The Annals of Mathematical Statistics, 12*(2), 236–239. https://doi.org/10.1214/aoms/1177731755
    
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
    >>> ts_sign_os(ex1, levels=order)
       p-value                  test
    0  0.01952  one-sample sign test
    
    Example 2: Numeric data
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> ts_sign_os(ex2)
        p-value                  test
    0  0.454498  one-sample sign test
    
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
    
    data = data.sort_values()
    
    #set hypothesized median to mid range if not provided
    if (mu is None):
        mu = (min(data) + max(data)) / 2
        
    #Determine count of cases below hypothesized median
    group1 = data[data<mu]
    group2 = data[data>mu]
    n1 = len(group1)
    n2 = len(group2)
    
    #Select the lowest of the two
    myMin = min(n1,n2)
    
    #Determine total number of cases (unequal to hyp. median)
    n = n1+n2
    
    #Determine the significance using binomial test
    pVal = 2*binom.cdf(myMin, n,0.5)
    if pVal > 1:
        pVal = 1
    testUsed = "one-sample sign test"
    testResults = pd.DataFrame([[pVal, testUsed]], columns=["p-value", "test"])
    pd.set_option('display.max_colwidth', None)
    
    return(testResults)