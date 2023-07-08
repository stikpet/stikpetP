import pandas as pd
import numpy as np

def me_consensus(data, levels=None):
    '''
    Consensus
    ---------
    
    The Consensus is a measure of agreement or dispersion for ordinal data. If there is no agreement the value is 0, and with full agreement 1.
    
    Parameters
    ----------
    data : list or pandas series 
    levels : dictionary, optional
        with coding to use
    
    Returns
    -------
    Cns : the consensus score
    
    Notes
    -----
    The formula used (Tastle et al., 2005, p. 98):
    $$\\text{Cns}\\left(X\\right) = 1 + \\sum_{i=1}^k p_i \\log_2\\left(1 - \\frac{\\left|X_i - \\mu_X\\right|}{d_X}\\right)$$
    
    With:
    $$\\mu_X = \\frac{\\sum_{i=1}^k X_i\\times F_i}{n}$$
    $$d_X = \\max\\left(X_i\\right) - \\min\\left(X_i\\right)$$
    $$p_i = \\frac{F_i}{n}$$
    
    *Symbols used:*
    
    * \\(X_i\\) the rank of category i
    * \\(F_i\\) the frequency (count) of the i-th category (after they have been sorted)
    * \\(n\\) the sample size
    * \\(k\\) the number of categories.
    
    References 
    ----------
    Tastle, W. J., & Wierman, M. J. (2007). Consensus and dissention: A measure of ordinal dispersion. *International Journal of Approximate Reasoning, 45*(3), 531–545. https://doi.org/10.1016/j.ijar.2006.06.024
    
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
    >>> me_consensus(ex1, levels=order)
    0.42896860013343574
    
    Example 2: Numeric data
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> me_consensus(ex2)
    0.3340394927779964

    '''
    
    if type(data) is list:
        data = pd.Series(data)
        
    data = data.dropna()
    if levels is not None:
        dataN = data.replace(levels)
        dataN = pd.to_numeric(dataN)
    else:
        dataN = pd.to_numeric(data)
    
    dataN = dataN.sort_values()
    
    myFreq = dataN.value_counts()
    myPs = myFreq / sum(myFreq)
    muX = dataN.mean()
    dX = dataN.max() - dataN.min()
    myCat = myFreq.index
    Cns = 1 + sum(myPs * np.log2(1 - abs(myCat - muX)/dX))
    
    return Cns