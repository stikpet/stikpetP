import pandas as pd

def es_dominance(data, levels=None, mu=None, out="dominance"):
    '''
    Dominance and a Vargha-Delaney A like effect size measure
    ---------------------------------------------------------
    
    This measure could be used with a sign test, since it does not rely on a z-value.
    
    Parameters
    ----------
    data : list or pandas data series 
        the data
    levels : dictionary, optional
        the categories and numeric value to use
    mu : float, optional 
        parameter to set the hypothesized median. If not used the midrange is used
    out : {"dominance", "vda"}, optional 
        to either show the "dominance" score (default), or a "vda" like measure
        
    Returns
    -------
    testResults : pandas dataframe 
        with mu and the requested value
   
    Notes
    -----
    The formula used is (Mangiafico, 2016, p. 223-224):
    $$D = p_{pos} - p_{neg}$$
    
    Where:
    $$p_i = \\frac{n_i}{n}$$
    
    *Symbols used:*
    
    * \\(p_{pos}\\) the proportion of cases above the hypothesized median
    * \\(p_{neg}\\) the proportion of cases below the hypothesized median
    * \\(n_{pos}\\) the number of cases above the hypothesized median
    * \\(n_{neg}\\) the number of cases below the hypothesized median
    * \\(n\\) the total number of cases
    
    The dominance score will range from -1 to 1.
    
    A Vargha-Delaney A (VDA) style effect size is calculated with (Mangiafico, 2016, p. 223-224):
    $$VDA_{like} = \\frac{D + 1}{2}$$
    
    This will range from 0 to 1, with 0.5 being the same as a dominance score of 0.
    
    References 
    ----------
    Mangiafico, S. S. (2016). Summary and analysis of extension program evaluation in R (1.20.01). Rutger Cooperative Extension.

    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: Text Pandas Series
    >>> import pandas as pd
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df2['Teach_Motivate']
    >>> order = {"Fully Disagree":1, "Disagree":2, "Neither disagree nor agree":3, "Agree":4, "Fully agree":5}
    >>> es_dominance(ex1, levels=order)
        mu  dominance
    0  3.0  -0.296296
    
    Example 2: Numeric data
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> es_dominance(ex2)
        mu  dominance
    0  3.0   0.222222
    
    
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
    if mu is None:
        mu = (min(data) + max(data)) / 2
        
    #total sample size
    n = len(data)
    
    #remove scores equal to hypothesized median
    dataRed = data[data != mu]
    
    pPlus = sum(data > mu)/n
    pMin = sum(data < mu)/n
    
    res = pPlus - pMin
    title = "dominance"
    
    if out=="vda":
        res = (res + 1)/2
        title = "VDA-like"
    
    #prepare results
    results = pd.DataFrame([[mu, res]], columns=["mu", title])        
    pd.set_option('display.max_colwidth', None)
    
    return(results)