import pandas as pd

def es_dominance(data, levels=None, mu=None, out="dominance"):
    '''
    Dominance and a Vargha-Delaney A like effect size measure
    
    This measure could be used with a sign test, since it does not rely on a z-value.
    
    Parameters
    ----------
    data : pandas data series with the data
    levels : optional dictionary with the categories and numeric value to use
    mu : optional parameter to set the hypothesized median. If not used the midrange is used
    out : optional to either show the "dominance" score (default), or a "vda" like measure
        
    Returns
    -------
    testResults : pandas dataframe with mu and the requested value
   
    Notes
    -----
    The formula used is (Mangiafico, 2016, p. 223-224):
    $$D = p_{pos} - p_{neg}$$
    
    Where:
    $$p_i = \\frac{n_i}{n}$$
    
    *Symbols used:*
    * \(p_{pos}\) the proportion of cases above the hypothesized median
    * \(p_{neg}\) the proportion of cases below the hypothesized median
    * \(n_{pos}\) the number of cases above the hypothesized median
    * \(n_{neg}\) the number of cases below the hypothesized median
    * \(n\) the total number of cases
    
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
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> dataList = [1, 2, 5, 1, 1, 5, 3, 1, 5, 1, 1, 5, 1, 1, 3, 3, 3, 4, 2, 4]
    >>> data = pd.Series(dataList)
    >>> es_dominance(data)
    >>> es_dominance(data, mu = 2)
    
    '''
    
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
        res = (dominance + 1)/2
        title = "VDA-like"
    
    #prepare results
    testResults = pd.DataFrame([[mu, res]], columns=["mu", title])        
    pd.set_option('display.max_colwidth', None)
    
    return(testResults)