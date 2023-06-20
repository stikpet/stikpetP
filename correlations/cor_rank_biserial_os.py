import pandas as pd

def r_rank_biserial_os(data, levels=None, mu=None):
    '''
    Rank biserial correlation coefficient (one-sample)
     
    This function will calculate Rank biserial correlation coefficient (one-sample)
    
    Parameters
    ----------
    data : pandas data series with the data
    levels : optional dictionary with the categories and numeric value to use
    mu : optional parameter to set the hypothesized median. If not used the midrange is used
        
    Returns
    -------
    testResults : Pandas dataframe with the hypothesized median and effect size.
    
    Notes
    -----
    The formula used (Kerby, 2014, p. 5):
    $$r_{rb} = \\frac{\\left|R_{pos} - R_{neg}\\right|}{R}$$
    
    This is actually the same as (King & Minium, 2008, p. 403):
    $$r_{rb} = \\frac{4\\times\\left|R_{min} - \\frac{R_{pos} + R_{min}}{2}\\right|}{n\\times\\left(n + 1\\right)}$$
    
    *Symbols used:*
    * \(R_{pos}\) the sum of the ranks with a positive deviation from the hypothesized median 
    * \(R_{neg}\) the sum of the ranks with a positive deviation from the hypothesized median 
    * \(R_{min}\) the minimum of \(R_{pos}}\),\(\\eqn{R_{neg}\)
    * \(n\) the number of ranks with a non-zero difference with the hypothesized median 
    * \(R\) the sum of all ranks, i.e. \(R_{pos} + R_{neg}\)
    
    If no hypothesized median is provided, the midrange is used, defined as:
    $$\\frac{x_{max} - x_{min}}{2}$$
    
    Where \(x_{max}\) is the maximum value of the scores, and \(x_{min}\) the minimum
    
    References 
    ----------
    Kerby, D. S. (2014). The simple difference formula: An approach to teaching nonparametric correlation. *Comprehensive Psychology*, 3, 1–9. https://doi.org/10.2466/11.IT.3.1
    
    King, B. M., & Minium, E. W. (2008). *Statistical reasoning in the behavioral sciences* (5th ed.). John Wiley & Sons, Inc.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> dataList = [1, 2, 5, 1, 1, 5, 3, 1, 5, 1, 1, 5, 1, 1, 3, 3, 3, 4, 2, 4]
    >>> data = pd.Series(dataList)
    >>> r_rank_biserial_os(data)
    >>> r_rank_biserial_os(data, mu = 2.5)
    
    '''
    #data as a pandas series
    
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
        
    #remove scores equal to hypothesized median
    rankDf = pd.DataFrame(data[data-mu != 0])
    
    #determine differences with mu and absolute values of those
    rankDf['diff'] = rankDf.iloc[:,0] - mu    
    rankDf['abs. diff.'] = abs(rankDf['diff'])
    
    #rank the absolute differences
    rankDf['ranks'] = rankDf['abs. diff.'].rank()
    
    #determine the sum of the positive and the negative ranks
    Rplus = rankDf.query("diff > 0")["ranks"].sum()
    Rmin = rankDf.query("diff < 0")["ranks"].sum()
    
    #calculate the rank biserial correlation
    rb = abs(Rplus - Rmin)/(Rplus + Rmin)
    
    #prepare results
    testResults = pd.DataFrame([[mu, rb]], columns=["mu", "rb"])        
    pd.set_option('display.max_colwidth', None)
    
    return testResults