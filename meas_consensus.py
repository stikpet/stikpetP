import pandas as pd
import numpy as np

def me_consensus(data, levels=None):
    '''
    Consensus
    
    The Consensus is a measure of agreement or dispersion for ordinal data. If there is no agreement the value is 0, and with full agreement 1.
    
    Parameters
    ----------
    data : pandas series with
    levels : optional dictionary with coding to use
    
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
    * \(X_i\) the rank of category i
    * \(F_i\) the frequency (count) of the i-th category (after they have been sorted)
    * \(n\) the sample size
    * \(k\) the number of categories.
    
    References 
    ----------
    Tastle, W. J., & Wierman, M. J. (2007). Consensus and dissention: A measure of ordinal dispersion. *International Journal of Approximate Reasoning, 45*(3), 531–545. https://doi.org/10.1016/j.ijar.2006.06.024
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet    
    
    '''
        
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