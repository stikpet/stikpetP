import pandas as pd

def es_alt_ratio(data, codes=None, p0=0.5, category=None):
    '''
    Alternative Ratio
     
    The Alternative Ratio is an effect size measure that could be accompanying a one-sample binomial, score or Wald test.It is simply the sample proportion (percentage), divided by the expected population proportion (often set at 0.5)
    
    The Alternative Ratio is only mentioned in the documentation of a program called PASS from NCSS (n.d.), and referred to as Relative Risk by JonB (2015).
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    codes : optional list with the two codes to use
    p0 : optional probability for first category
    category : optional the category to count as first category
        
    Returns
    -------
    testResults : Pandas dataframe with the two Alternative Ratios.
   
    Notes
    -----
    If codes and category are not provided the first category will be the first data point
    
    If codes only are provided the first category in the codes is used.
    
    The formula used is:
    $$AR=\\frac{p}{\\pi}$$
    
    *Symbols used*:
    * \(p\) is the sample proportion of one of the categories
    * \(\\pi\) the expected proportion
    
    References
    ----------
    JonB. (2015, October 14). Effect size of a binomial test and its relation to other measures of effect size. StackExchange - Cross Validated. https://stats.stackexchange.com/q/176856
    
    NCSS. (n.d.). Tests for one proportion. In PASS Sample Size Software (pp. 100-1-100–132). Retrieved November 10, 2018, from https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/PASS/Tests_for_One_Proportion.pdf
    
    Examples
    --------
    >>> dataList = ["Female", "Male", "Male", "Female", "Male", "Male"]
    >>> data = pd.Series(dataList)
    >>> es_alt_ratio(data)
    >>> es_alt_ratio(data, category='Male')
    >>> es_alt_ratio(data, codes=['Female', 'Male'])


    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    if codes is None:
        freq = data.value_counts()
        n = sum(freq.values)
        
        if category is None:
            n1 = freq.values[0] 
        else:
            n1 = sum(data==category)
        
        n2 = n - n1
        
    else:
        #Determine number of successes
        n1 = sum(data==codes[0])
        n2 = sum(data==codes[1])
        n = n1 + n2
        
        if not(category is None):
            n3 = n1
            n1 = n2
            n2 = n3
        
    p1 = n1 / n
    p2 = n2 / n
    AR1 = p1 / p0
    AR2 = p2 / (1 - p0)
    
    testResults = pd.DataFrame([[AR1, AR2]], columns=["Alt.Ratio Cat. 1", "Alt.Ratio Cat. 2"])
    
    return (testResults)