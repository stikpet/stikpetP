import pandas as pd

def es_alt_ratio(data, codes=None, p0=0.5, category=None):
    '''
    Alternative Ratio
    -----------------
     
    The Alternative Ratio is an effect size measure that could be accompanying a one-sample binomial, score or Wald test.It is simply the sample proportion (percentage), divided by the expected population proportion (often set at 0.5)
    
    The Alternative Ratio is only mentioned in the documentation of a program called PASS from NCSS (n.d.), and referred to as Relative Risk by JonB (2015).
    
    Parameters
    ----------
    data : list or pandas data series 
        the data
    codes : list, optional 
        the two codes to use
    p0 : float, optional 
        probability for first category. Default is 0.5
    category : optional the category to count as first category
        
    Returns
    -------
    results : pandas dataframe with:
    
    * *AR1*, the alternative category for one category
    * *AR2*, the alternative category for the other category
   
    Notes
    -----
    If codes and category are not provided the first category will be the first data point
    
    If codes only are provided the first category in the codes is used.
    
    The formula used is:
    $$AR=\\frac{p}{\\pi}$$
    
    *Symbols used*:
    
    * \\(p\\) is the sample proportion of one of the categories
    * \\(\\pi\\) the expected proportion
    
    References
    ----------
    JonB. (2015, October 14). Effect size of a binomial test and its relation to other measures of effect size. StackExchange - Cross Validated. https://stats.stackexchange.com/q/176856
    
    NCSS. (n.d.). Tests for one proportion. In PASS Sample Size Software (pp. 100-1-100–132). Retrieved November 10, 2018, from https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/PASS/Tests_for_One_Proportion.pdf
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    
    Example 1: Numeric list
    >>> ex1 = [1, 1, 2, 1, 2, 1, 2, 1]
    >>> es_alt_ratio(ex1)
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0              1.25              0.75
    
    >>> es_alt_ratio(ex1, p0=0.3)
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0          2.083333          0.535714
    
    Example 2: Text list
    >>> ex2 = ["Female", "Male", "Male", "Female", "Male", "Male"]
    >>> es_alt_ratio(ex2)
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0          1.333333          0.666667
    
    >>> es_alt_ratio(ex2, category='Female')
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0          0.666667          1.333333
    
    >>> es_alt_ratio(ex2, codes=['Female', 'Male'])
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0          0.666667          1.333333
    
    Example 3: pandas Series
    >>> import pandas as pd
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> es_alt_ratio(df1['sex'])
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0           1.10233           0.89767

    >>> es_alt_ratio(df1['mar1'], codes=["DIVORCED", "NEVER MARRIED"])
       Alt.Ratio Cat. 1  Alt.Ratio Cat. 2
    0          0.885755          1.114245
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
        
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
    
    results = pd.DataFrame([[AR1, AR2]], columns=["Alt.Ratio Cat. 1", "Alt.Ratio Cat. 2"])
    
    return (results)